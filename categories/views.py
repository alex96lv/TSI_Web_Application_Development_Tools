from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def category_list(request):
    """List all categories or create new one"""
    if request.method == 'GET':
        categories = Category.objects(user=request.user_obj)

        # Filter by type if provided
        category_type = request.GET.get('type')
        if category_type in ['income', 'expense']:
            categories = categories.filter(type=category_type)

        data = [cat.to_dict() for cat in categories]
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            category = serializer.save()
            return Response(category.to_dict(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def category_detail(request, pk):
    """Retrieve, update or delete a category"""
    try:
        category = Category.objects(id=pk, user=request.user_obj).first()
        if not category:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Некорректный ID'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return Response(category.to_dict(), status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            category = serializer.save()
            return Response(category.to_dict(), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if category.is_default:
            return Response({'error': 'Нельзя удалить стандартную категорию'}, status=status.HTTP_400_BAD_REQUEST)

        category.delete()
        return Response({'message': 'Категория удалена'}, status=status.HTTP_204_NO_CONTENT)
