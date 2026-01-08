from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User profile
    path('me/', views.get_current_user, name='current_user'),
    path('update/', views.update_user, name='update_user'),
    path('change-password/', views.change_password, name='change_password'),

    # Password reset
    path('password-reset/request/', views.password_reset_request, name='password_reset_request'),
    path('password-reset/verify-security/', views.password_reset_with_security_question, name='password_reset_security'),
    path('password-reset/verify-code/', views.password_reset_with_code, name='password_reset_code'),
]
