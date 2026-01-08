from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Goal
from .serializers import GoalSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def goal_list(request):
    """List all goals or create new one"""
    if request.method == 'GET':
        goals = Goal.objects(user=request.user_obj).order_by('-created_at')

        goal_status = request.GET.get('status')
        if goal_status in ['active', 'achieved', 'cancelled']:
            goals = goals.filter(status=goal_status)

        data = [g.to_dict() for g in goals]
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = GoalSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            goal = serializer.save()
            return Response(goal.to_dict(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def goal_detail(request, pk):
    """Retrieve, update or delete a goal"""
    try:
        goal = Goal.objects(id=pk, user=request.user_obj).first()
        if not goal:
            return Response({'error': 'Цель не найдена'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Некорректный ID'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return Response(goal.to_dict(), status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = GoalSerializer(goal, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            goal = serializer.save()

            # Check if goal is achieved
            if goal.current_amount >= goal.target_amount and goal.status == 'active':
                goal.status = 'achieved'
                goal.save()

            return Response(goal.to_dict(), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        goal.delete()
        return Response({'message': 'Цель удалена'}, status=status.HTTP_204_NO_CONTENT)
