from mongoengine import Document, StringField, EmailField, DateTimeField, BooleanField, ReferenceField
from datetime import datetime, timedelta
import bcrypt
import secrets
import string


class User(Document):
    """User model for authentication and user management"""

    email = EmailField(required=True, unique=True)
    password_hash = StringField(required=True)
    first_name = StringField(max_length=100)
    last_name = StringField(max_length=100)
    currency = StringField(max_length=3, default='EUR', choices=['USD', 'EUR'])
    theme = StringField(max_length=10, default='light', choices=['light', 'dark'])
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    # Security question for password recovery
    security_question = StringField(max_length=255)
    security_answer_hash = StringField()

    meta = {
        'collection': 'users',
        'indexes': [
            'email',
            'created_at'
        ]
    }

    def set_password(self, password):
        """Hash and set user password"""
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password_bytes, salt).decode('utf-8')

    def check_password(self, password):
        """Check if provided password matches the hash"""
        password_bytes = password.encode('utf-8')
        password_hash_bytes = self.password_hash.encode('utf-8')
        return bcrypt.checkpw(password_bytes, password_hash_bytes)

    def set_security_answer(self, answer):
        """Hash and set security answer"""
        answer_bytes = answer.lower().strip().encode('utf-8')
        salt = bcrypt.gensalt()
        self.security_answer_hash = bcrypt.hashpw(answer_bytes, salt).decode('utf-8')

    def check_security_answer(self, answer):
        """Check if provided answer matches the hash"""
        if not self.security_answer_hash:
            return False
        answer_bytes = answer.lower().strip().encode('utf-8')
        answer_hash_bytes = self.security_answer_hash.encode('utf-8')
        return bcrypt.checkpw(answer_bytes, answer_hash_bytes)

    def get_full_name(self):
        """Get user's full name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email

    @property
    def is_authenticated(self):
        """Always return True for authenticated users (required by DRF)"""
        return True

    @property
    def is_anonymous(self):
        """Always return False for authenticated users"""
        return False

    def to_dict(self):
        """Convert user to dictionary (excluding password)"""
        return {
            'id': str(self.id),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'currency': self.currency,
            'theme': self.theme,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __str__(self):
        return self.email


class PasswordResetCode(Document):
    """Temporary password reset code"""

    user = ReferenceField(User, required=True)
    reset_code = StringField(required=True, max_length=8)
    created_at = DateTimeField(default=datetime.utcnow)
    expires_at = DateTimeField(required=True)
    is_used = BooleanField(default=False)

    meta = {
        'collection': 'password_reset_codes',
        'indexes': [
            'reset_code',
            'expires_at',
            'user'
        ]
    }

    @staticmethod
    def generate_code():
        """Generate random 8-character code"""
        alphabet = string.ascii_uppercase + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(8))

    @classmethod
    def create_for_user(cls, user):
        """Create new reset code for user"""
        # Invalidate existing codes
        cls.objects(user=user, is_used=False).update(is_used=True)

        # Generate new code
        code = cls.generate_code()
        reset_code = cls(
            user=user,
            reset_code=code,
            expires_at=datetime.utcnow() + timedelta(minutes=15)
        )
        reset_code.save()
        return reset_code

    def is_valid(self):
        """Check if code is still valid"""
        return not self.is_used and datetime.utcnow() < self.expires_at

    def __str__(self):
        return f"{self.reset_code} for {self.user.email}"
