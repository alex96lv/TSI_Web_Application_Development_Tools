from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions
from .models import User


class MongoJWTAuthentication(JWTAuthentication):
    """Custom JWT Authentication for MongoDB"""

    def get_user(self, validated_token):
        """
        Get user from MongoDB using user_id from JWT token
        """
        try:
            user_id = validated_token.get('user_id')
            if not user_id:
                raise exceptions.AuthenticationFailed('Token does not contain user_id')

            user = User.objects(id=user_id).first()
            if not user:
                raise exceptions.AuthenticationFailed('User not found')

            if not user.is_active:
                raise exceptions.AuthenticationFailed('User is inactive')

            return user

        except Exception as e:
            raise exceptions.AuthenticationFailed(f'Authentication failed: {str(e)}')


class MongoAuthMiddleware:
    """Middleware to add MongoDB user object to request"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Try to authenticate with JWT
        auth = MongoJWTAuthentication()
        try:
            user_auth = auth.authenticate(request)
            if user_auth is not None:
                request.user_obj = user_auth[0]
        except:
            request.user_obj = None

        response = self.get_response(request)
        return response
