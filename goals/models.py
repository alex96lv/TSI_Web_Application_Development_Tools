from mongoengine import (
    Document, StringField, FloatField, ReferenceField,
    DateTimeField
)
from datetime import datetime


class Goal(Document):
    """Goal model for savings targets"""

    user = ReferenceField('User', required=True)
    name = StringField(required=True, max_length=200)
    target_amount = FloatField(required=True, min_value=0)
    current_amount = FloatField(default=0, min_value=0)
    deadline = DateTimeField()
    status = StringField(
        required=True,
        choices=['active', 'achieved', 'cancelled'],
        default='active'
    )
    description = StringField(max_length=1000)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'goals',
        'indexes': [
            'user',
            'status',
            'deadline',
            '-created_at'
        ]
    }

    def get_progress_percentage(self):
        """Calculate progress percentage"""
        if self.target_amount > 0:
            return round((self.current_amount / self.target_amount) * 100, 2)
        return 0

    def get_remaining_amount(self):
        """Get remaining amount to reach goal"""
        return max(0, self.target_amount - self.current_amount)

    def to_dict(self):
        """Convert goal to dictionary"""
        return {
            'id': str(self.id),
            'name': self.name,
            'target_amount': self.target_amount,
            'current_amount': self.current_amount,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'status': self.status,
            'description': self.description,
            'progress_percentage': self.get_progress_percentage(),
            'remaining_amount': self.get_remaining_amount(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __str__(self):
        return f"{self.name} ({self.get_progress_percentage()}%)"
