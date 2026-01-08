from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import RecurringTransaction
from .serializers import RecurringTransactionSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def recurring_transaction_list(request):
    """List all recurring transactions or create new one"""
    if request.method == 'GET':
        recurring_transactions = RecurringTransaction.objects(user=request.user_obj).order_by('-created_at')

        # Filters
        trans_type = request.GET.get('type')
        is_active = request.GET.get('is_active')

        if trans_type in ['income', 'expense']:
            recurring_transactions = recurring_transactions.filter(type=trans_type)

        if is_active is not None:
            is_active_bool = is_active.lower() == 'true'
            recurring_transactions = recurring_transactions.filter(is_active=is_active_bool)

        data = [rt.to_dict() for rt in recurring_transactions]
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = RecurringTransactionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            recurring_transaction = serializer.save()
            return Response(recurring_transaction.to_dict(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def recurring_transaction_detail(request, pk):
    """Retrieve, update or delete a recurring transaction"""
    try:
        recurring_transaction = RecurringTransaction.objects(id=pk, user=request.user_obj).first()
        if not recurring_transaction:
            return Response({'error': 'Повторяющаяся транзакция не найдена'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Некорректный ID'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return Response(recurring_transaction.to_dict(), status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = RecurringTransactionSerializer(
            recurring_transaction,
            data=request.data,
            context={'request': request},
            partial=True
        )
        if serializer.is_valid():
            recurring_transaction = serializer.save()
            return Response(recurring_transaction.to_dict(), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recurring_transaction.delete()
        return Response({'message': 'Повторяющаяся транзакция удалена'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_recurring_transaction(request, pk):
    """Toggle active/inactive status of a recurring transaction"""
    try:
        recurring_transaction = RecurringTransaction.objects(id=pk, user=request.user_obj).first()
        if not recurring_transaction:
            return Response({'error': 'Повторяющаяся транзакция не найдена'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Некорректный ID'}, status=status.HTTP_400_BAD_REQUEST)

    recurring_transaction.is_active = not recurring_transaction.is_active
    recurring_transaction.save()

    return Response(recurring_transaction.to_dict(), status=status.HTTP_200_OK)
