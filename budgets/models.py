from mongoengine import (
    Document, StringField, FloatField, ReferenceField,
    DateTimeField, BooleanField
)
from datetime import datetime


class Budget(Document):
    """Budget model for tracking spending limits per category"""

    user = ReferenceField('User', required=True)
    category = ReferenceField('Category', required=True)
    limit_amount = FloatField(required=True, min_value=0)
    period = StringField(required=True, choices=['weekly', 'monthly'], default='monthly')
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'budgets',
        'indexes': [
            'user',
            'category',
            'period',
            'is_active'
        ]
    }

    def to_dict(self):
        """Convert budget to dictionary"""
        return {
            'id': str(self.id),
            'limit_amount': self.limit_amount,
            'period': self.period,
            'is_active': self.is_active,
            'category': {
                'id': str(self.category.id),
                'name': self.category.name,
                'name_translations': self.category.name_translations or {},
                'icon': self.category.icon,
                'color': self.category.color,
            } if self.category else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __str__(self):
        return f"Budget: {self.category.name} - {self.limit_amount} ({self.period})"
