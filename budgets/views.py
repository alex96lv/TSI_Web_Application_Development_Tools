from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Budget
from .serializers import BudgetSerializer
from transactions.models import Transaction
from datetime import datetime, timedelta


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def budget_list(request):
    """List all budgets or create new one"""
    if request.method == 'GET':
        budgets = Budget.objects(user=request.user_obj, is_active=True)
        data = []

        for budget in budgets:
            budget_dict = budget.to_dict()

            # Calculate spent amount
            now = datetime.utcnow()
            if budget.period == 'weekly':
                start_date = now - timedelta(days=7)
            else:  # monthly
                start_date = datetime(now.year, now.month, 1)

            spent = sum([t.amount for t in Transaction.objects(
                user=request.user_obj,
                category=budget.category,
                type='expense',
                date__gte=start_date
            )])

            budget_dict['spent'] = spent
            budget_dict['remaining'] = max(0, budget.limit_amount - spent)
            budget_dict['percentage'] = round((spent / budget.limit_amount * 100), 2) if budget.limit_amount > 0 else 0

            data.append(budget_dict)

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BudgetSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            budget = serializer.save()
            return Response(budget.to_dict(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def budget_detail(request, pk):
    """Retrieve, update or delete a budget"""
    try:
        budget = Budget.objects(id=pk, user=request.user_obj).first()
        if not budget:
            return Response({'error': 'Бюджет не найден'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Некорректный ID'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return Response(budget.to_dict(), status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = BudgetSerializer(budget, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            budget = serializer.save()
            return Response(budget.to_dict(), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        budget.delete()
        return Response({'message': 'Бюджет удалён'}, status=status.HTTP_204_NO_CONTENT)
