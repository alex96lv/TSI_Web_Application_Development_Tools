from mongoengine import (
    Document, StringField, FloatField, ReferenceField,
    DateTimeField, ListField
)
from datetime import datetime


class Transaction(Document):
    """Transaction model for income and expense tracking"""

    user = ReferenceField('User', required=True)
    category = ReferenceField('Category', required=True)
    type = StringField(required=True, choices=['income', 'expense'])
    amount = FloatField(required=True, min_value=0)
    description = StringField(max_length=500)
    date = DateTimeField(required=True, default=datetime.utcnow)
    tags = ListField(StringField(max_length=50))
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'transactions',
        'indexes': [
            'user',
            'category',
            'type',
            'date',
            '-created_at'  # Descending order for recent transactions
        ]
    }

    def to_dict(self):
        """Convert transaction to dictionary"""
        return {
            'id': str(self.id),
            'type': self.type,
            'amount': self.amount,
            'description': self.description,
            'date': self.date.isoformat() if self.date else None,
            'category': {
                'id': str(self.category.id),
                'name': self.category.name,
                'name_translations': self.category.name_translations or {},
                'icon': self.category.icon,
                'color': self.category.color,
            } if self.category else None,
            'tags': self.tags,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __str__(self):
        return f"{self.type.upper()}: {self.amount} - {self.description[:30]}"
