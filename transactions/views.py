from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Transaction
from .serializers import TransactionSerializer
from datetime import datetime, timedelta
import csv
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def transaction_list(request):
    """List all transactions or create new one"""
    if request.method == 'GET':
        transactions = Transaction.objects(user=request.user_obj).order_by('-date')

        # Filters
        trans_type = request.GET.get('type')
        category_id = request.GET.get('category')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if trans_type in ['income', 'expense']:
            transactions = transactions.filter(type=trans_type)

        if category_id:
            transactions = transactions.filter(category=category_id)

        if start_date:
            transactions = transactions.filter(date__gte=datetime.fromisoformat(start_date))

        if end_date:
            transactions = transactions.filter(date__lte=datetime.fromisoformat(end_date))

        data = [t.to_dict() for t in transactions]
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            transaction = serializer.save()
            return Response(transaction.to_dict(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def transaction_detail(request, pk):
    """Retrieve, update or delete a transaction"""
    try:
        transaction = Transaction.objects(id=pk, user=request.user_obj).first()
        if not transaction:
            return Response({'error': 'Транзакция не найдена'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Некорректный ID'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return Response(transaction.to_dict(), status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            transaction = serializer.save()
            return Response(transaction.to_dict(), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response({'message': 'Транзакция удалена'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transaction_stats(request):
    """Get transaction statistics"""
    user = request.user_obj

    # Get current month transactions
    now = datetime.utcnow()
    start_of_month = datetime(now.year, now.month, 1)

    income_total = sum([t.amount for t in Transaction.objects(user=user, type='income', date__gte=start_of_month)])
    expense_total = sum([t.amount for t in Transaction.objects(user=user, type='expense', date__gte=start_of_month)])

    return Response({
        'current_month': {
            'income': income_total,
            'expense': expense_total,
            'balance': income_total - expense_total
        }
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_csv(request):
    """Export transactions to CSV"""
    user = request.user_obj
    transactions = Transaction.objects(user=user).order_by('-date')

    # Get language from query parameter
    lang = request.GET.get('lang', 'ru')

    # Translations
    translations = {
        'ru': {
            'date': 'Дата',
            'type': 'Тип',
            'category': 'Категория',
            'amount': 'Сумма',
            'description': 'Описание',
            'income': 'Доход',
            'expense': 'Расход'
        },
        'en': {
            'date': 'Date',
            'type': 'Type',
            'category': 'Category',
            'amount': 'Amount',
            'description': 'Description',
            'income': 'Income',
            'expense': 'Expense'
        },
        'lv': {
            'date': 'Datums',
            'type': 'Tips',
            'category': 'Kategorija',
            'amount': 'Summa',
            'description': 'Apraksts',
            'income': 'Ieņēmumi',
            'expense': 'Izdevumi'
        }
    }

    t = translations.get(lang, translations['ru'])

    # Apply same filters as in transaction_list
    trans_type = request.GET.get('type')
    category_id = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if trans_type in ['income', 'expense']:
        transactions = transactions.filter(type=trans_type)

    if category_id:
        transactions = transactions.filter(category=category_id)

    if start_date:
        transactions = transactions.filter(date__gte=datetime.fromisoformat(start_date))

    if end_date:
        transactions = transactions.filter(date__lte=datetime.fromisoformat(end_date))

    # Create CSV response
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="transactions_{datetime.now().strftime("%Y%m%d")}.csv"'
    response.write('\ufeff')  # UTF-8 BOM for Excel compatibility

    writer = csv.writer(response)
    writer.writerow([t['date'], t['type'], t['category'], t['amount'], t['description']])

    for transaction in transactions:
        category_name = transaction.category.get_name(lang) if transaction.category else '-'
        trans_type_label = t['income'] if transaction.type == 'income' else t['expense']
        writer.writerow([
            transaction.date.strftime('%Y-%m-%d %H:%M'),
            trans_type_label,
            category_name,
            f'{transaction.amount:.2f}',
            transaction.description or ''
        ])

    return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_pdf(request):
    """Export transactions to PDF"""
    user = request.user_obj
    transactions = Transaction.objects(user=user).order_by('-date')

    # Get language from query parameter or user preference
    lang = request.GET.get('lang', user.language if hasattr(user, 'language') else 'ru')

    # Translations
    translations = {
        'ru': {
            'title': 'Отчёт по транзакциям',
            'summary': 'Итоги',
            'total_income': 'Всего доходов',
            'total_expense': 'Всего расходов',
            'balance': 'Баланс',
            'transactions': 'Транзакции',
            'date': 'Дата',
            'type': 'Тип',
            'category': 'Категория',
            'description': 'Описание',
            'amount': 'Сумма',
            'income': 'Доход',
            'expense': 'Расход'
        },
        'en': {
            'title': 'Transaction Report',
            'summary': 'Summary',
            'total_income': 'Total Income',
            'total_expense': 'Total Expenses',
            'balance': 'Balance',
            'transactions': 'Transactions',
            'date': 'Date',
            'type': 'Type',
            'category': 'Category',
            'description': 'Description',
            'amount': 'Amount',
            'income': 'Income',
            'expense': 'Expense'
        },
        'lv': {
            'title': 'Transakciju pārskats',
            'summary': 'Kopsavilkums',
            'total_income': 'Kopā ieņēmumi',
            'total_expense': 'Kopā izdevumi',
            'balance': 'Bilance',
            'transactions': 'Transakcijas',
            'date': 'Datums',
            'type': 'Tips',
            'category': 'Kategorija',
            'description': 'Apraksts',
            'amount': 'Summa',
            'income': 'Ieņēmumi',
            'expense': 'Izdevumi'
        }
    }

    t = translations.get(lang, translations['ru'])

    # Apply same filters as in transaction_list
    trans_type = request.GET.get('type')
    category_id = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if trans_type in ['income', 'expense']:
        transactions = transactions.filter(type=trans_type)

    if category_id:
        transactions = transactions.filter(category=category_id)

    if start_date:
        transactions = transactions.filter(date__gte=datetime.fromisoformat(start_date))

    if end_date:
        transactions = transactions.filter(date__lte=datetime.fromisoformat(end_date))

    # Register DejaVu font for Unicode support (Cyrillic, etc.)
    try:
        # Try to register DejaVu font if available
        from reportlab.pdfbase.pdfmetrics import registerFont
        from reportlab.pdfbase.ttfonts import TTFont
        import os

        # Common paths for DejaVu font
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/dejavu/DejaVuSans.ttf',
            'C:\\Windows\\Fonts\\DejaVuSans.ttf',
        ]

        font_registered = False
        for font_path in font_paths:
            if os.path.exists(font_path):
                registerFont(TTFont('DejaVu', font_path))
                font_name = 'DejaVu'
                font_registered = True
                break

        if not font_registered:
            # Fallback to Helvetica (won't show Cyrillic properly)
            font_name = 'Helvetica'
    except Exception as e:
        # Fallback to Helvetica
        font_name = 'Helvetica'

    # Create PDF
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30, leftMargin=30,
                            topMargin=30, bottomMargin=18)

    elements = []
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        fontName=font_name,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30,
        alignment=1  # Center
    )

    # Title
    title = Paragraph(t['title'], title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Summary
    total_income = sum([t.amount for t in transactions if t.type == 'income'])
    total_expense = sum([t.amount for t in transactions if t.type == 'expense'])
    balance = total_income - total_expense

    summary_data = [
        [t['total_income'] + ':', f'{total_income:.2f} {user.currency}'],
        [t['total_expense'] + ':', f'{total_expense:.2f} {user.currency}'],
        [t['balance'] + ':', f'{balance:.2f} {user.currency}']
    ]
    summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f3f4f6')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1, 20))

    # Transactions table
    data = [[t['date'], t['type'], t['category'], t['amount'], t['description']]]

    for transaction in transactions:
        category_name = transaction.category.get_name(lang) if transaction.category else '-'
        trans_type_label = t['income'] if transaction.type == 'income' else t['expense']
        data.append([
            transaction.date.strftime('%Y-%m-%d'),
            trans_type_label,
            category_name,
            f'{transaction.amount:.2f}',
            transaction.description[:30] if transaction.description else '-'
        ])

    table = Table(data, colWidths=[1.5*inch, 1*inch, 1.5*inch, 1*inch, 2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    elements.append(table)

    # Build PDF
    doc.build(elements)

    # Create response
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="transactions_report_{datetime.now().strftime("%Y%m%d")}.pdf"'

    return response
