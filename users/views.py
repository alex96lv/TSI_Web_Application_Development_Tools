from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, PasswordResetCode
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    PasswordResetRequestSerializer,
    PasswordResetVerifySerializer,
    PasswordResetWithCodeSerializer
)
from categories.models import Category
import logging

logger = logging.getLogger(__name__)


# Default categories for new users
DEFAULT_EXPENSE_CATEGORIES = [
    {
        'name': 'Еда и продукты',
        'name_translations': {'ru': 'Еда и продукты', 'en': 'Food & Groceries', 'lv': 'Pārtika un pārtikas produkti'},
        'icon': '🍽️',
        'color': '#f97316'  # Orange
    },
    {
        'name': 'Транспорт',
        'name_translations': {'ru': 'Транспорт', 'en': 'Transport', 'lv': 'Transports'},
        'icon': '🚙',
        'color': '#3b82f6'  # Blue
    },
    {
        'name': 'Жильё',
        'name_translations': {'ru': 'Жильё', 'en': 'Housing', 'lv': 'Mājoklis'},
        'icon': '🏡',
        'color': '#8b5cf6'  # Purple
    },
    {
        'name': 'Здоровье',
        'name_translations': {'ru': 'Здоровье', 'en': 'Health', 'lv': 'Veselība'},
        'icon': '💚',
        'color': '#10b981'  # Green
    },
    {
        'name': 'Развлечения',
        'name_translations': {'ru': 'Развлечения', 'en': 'Entertainment', 'lv': 'Izklaide'},
        'icon': '🎭',
        'color': '#ec4899'  # Pink
    },
    {
        'name': 'Прочее',
        'name_translations': {'ru': 'Прочее', 'en': 'Other', 'lv': 'Cits'},
        'icon': '📦',
        'color': '#64748b'  # Slate
    },
]

DEFAULT_INCOME_CATEGORIES = [
    {
        'name': 'Зарплата',
        'name_translations': {'ru': 'Зарплата', 'en': 'Salary', 'lv': 'Alga'},
        'icon': '💼',
        'color': '#10b981'  # Green
    },
    {
        'name': 'Фриланс',
        'name_translations': {'ru': 'Фриланс', 'en': 'Freelance', 'lv': 'Brīvprātīgais darbs'},
        'icon': '💻',
        'color': '#06b6d4'  # Cyan
    },
    {
        'name': 'Прочее',
        'name_translations': {'ru': 'Прочее', 'en': 'Other', 'lv': 'Cits'},
        'icon': '✨',
        'color': '#8b5cf6'  # Purple
    },
]


def create_default_categories(user):
    """Create default categories for new user"""
    for cat_data in DEFAULT_EXPENSE_CATEGORIES:
        category = Category(
            user=user,
            type='expense',
            is_default=True,
            **cat_data
        )
        category.save()

    for cat_data in DEFAULT_INCOME_CATEGORIES:
        category = Category(
            user=user,
            type='income',
            is_default=True,
            **cat_data
        )
        category.save()


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Register new user"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        # Create default categories
        create_default_categories(user)

        # Generate JWT tokens
        refresh = RefreshToken()
        refresh['user_id'] = str(user.id)
        refresh['email'] = user.email

        return Response({
            'message': 'Регистрация прошла успешно',
            'user': user.to_dict(),
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """Login user"""
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = User.objects(email=email).first()
        if not user or not user.check_password(password):
            return Response({
                'error': 'Неверный email или пароль'
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({
                'error': 'Аккаунт деактивирован'
            }, status=status.HTTP_403_FORBIDDEN)

        # Generate JWT tokens
        refresh = RefreshToken()
        refresh['user_id'] = str(user.id)
        refresh['email'] = user.email

        return Response({
            'message': 'Вход выполнен успешно',
            'user': user.to_dict(),
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    """Get current authenticated user"""
    user = request.user_obj
    return Response(user.to_dict(), status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    """Update user profile"""
    user = request.user_obj
    serializer = UserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Профиль обновлён',
            'user': user.to_dict()
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    """Change user password"""
    user = request.user_obj
    serializer = ChangePasswordSerializer(data=request.data)

    if serializer.is_valid():
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']

        if not user.check_password(old_password):
            return Response({
                'error': 'Неверный старый пароль'
            }, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({
            'message': 'Пароль успешно изменён'
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
@permission_classes([AllowAny])
def password_reset_request(request):
    """Request password reset - generates temporary code"""
    serializer = PasswordResetRequestSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        user = User.objects(email=email).first()

        if not user:
            # Dont reveal if user exists for security
            return Response({
                "message": "Если пользователь с таким email существует, код для сброса пароля был создан"
            }, status=status.HTTP_200_OK)

        # Create reset code
        reset_code = PasswordResetCode.create_for_user(user)

        # Log the code to console (for demo purposes)
        logger.warning(f"🔑 PASSWORD RESET CODE for {user.email}: {reset_code.reset_code}")
        logger.warning(f"⏰ Code expires in 15 minutes")
        print("\n" + "="*60)
        print(f"🔑 PASSWORD RESET CODE")
        print(f"📧 Email: {user.email}")
        print(f"🔐 Code: {reset_code.reset_code}")
        expires_str = reset_code.expires_at.strftime("%Y-%m-%d %H:%M:%S")
        print(f"⏰ Expires: {expires_str}")
        print("="*60 + "\n")

        return Response({
            "message": "Код для сброса пароля создан. Проверьте консоль сервера.",
            "security_question": user.security_question
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def password_reset_with_security_question(request):
    """Reset password using security question"""
    serializer = PasswordResetVerifySerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        security_answer = serializer.validated_data["security_answer"]
        new_password = serializer.validated_data["new_password"]

        user = User.objects(email=email).first()
        if not user:
            return Response({
                "error": "Неверный email или ответ на секретный вопрос"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Check security answer
        if not user.check_security_answer(security_answer):
            logger.warning(f"Failed password reset attempt for {email} - wrong security answer")
            return Response({
                "error": "Неверный email или ответ на секретный вопрос"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Reset password
        user.set_password(new_password)
        user.save()

        logger.info(f"Password reset successful for {email} using security question")
        return Response({
            "message": "Пароль успешно изменён"
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def password_reset_with_code(request):
    """Reset password using temporary code"""
    serializer = PasswordResetWithCodeSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        reset_code_str = serializer.validated_data["reset_code"]
        new_password = serializer.validated_data["new_password"]

        user = User.objects(email=email).first()
        if not user:
            return Response({
                "error": "Неверный email или код"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Find valid reset code
        reset_code = PasswordResetCode.objects(
            user=user,
            reset_code=reset_code_str,
            is_used=False
        ).first()

        if not reset_code or not reset_code.is_valid():
            logger.warning(f"Failed password reset attempt for {email} - invalid code")
            return Response({
                "error": "Неверный или истекший код"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Reset password
        user.set_password(new_password)
        user.save()

        # Mark code as used
        reset_code.is_used = True
        reset_code.save()

        logger.info(f"Password reset successful for {email} using temporary code")
        return Response({
            "message": "Пароль успешно изменён"
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

