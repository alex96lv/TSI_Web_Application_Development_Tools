from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserRegistrationSerializer(serializers.Serializer):
    """Serializer for user registration"""
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    currency = serializers.ChoiceField(choices=['USD', 'EUR'], default='USD')
    security_question = serializers.CharField(max_length=255, required=True)
    security_answer = serializers.CharField(write_only=True, required=True)

    def validate_email(self, value):
        """Check if email already exists"""
        if User.objects(email=value).first():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")
        return value

    def validate(self, attrs):
        """Check if passwords match"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})
        return attrs

    def create(self, validated_data):
        """Create new user"""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        security_answer = validated_data.pop('security_answer')

        user = User(**validated_data)
        user.set_password(password)
        user.set_security_answer(security_answer)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)


class UserSerializer(serializers.Serializer):
    """Serializer for user data"""
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    first_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    currency = serializers.ChoiceField(choices=['USD', 'EUR'])
    theme = serializers.ChoiceField(choices=['light', 'dark'])
    created_at = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        """Update user data"""
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.theme = validated_data.get('theme', instance.theme)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer for changing password"""
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        """Check if new passwords match"""
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({"new_password": "Новые пароли не совпадают."})
        return attrs


class PasswordResetRequestSerializer(serializers.Serializer):
    """Serializer for password reset request"""
    email = serializers.EmailField(required=True)


class PasswordResetVerifySerializer(serializers.Serializer):
    """Serializer for verifying security answer"""
    email = serializers.EmailField(required=True)
    security_answer = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        """Check if new passwords match"""
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({"new_password": "Новые пароли не совпадают."})
        return attrs


class PasswordResetWithCodeSerializer(serializers.Serializer):
    """Serializer for password reset with temporary code"""
    email = serializers.EmailField(required=True)
    reset_code = serializers.CharField(required=True, max_length=8)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        """Check if new passwords match"""
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({"new_password": "Новые пароли не совпадают."})
        return attrs
