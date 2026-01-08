from mongoengine import (
    Document, StringField, FloatField, ReferenceField,
    DateTimeField, BooleanField, IntField
)
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class RecurringTransaction(Document):
    """Recurring transaction model for automatic scheduled payments"""

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ]

    user = ReferenceField('User', required=True)
    category = ReferenceField('Category', required=True)
    type = StringField(required=True, choices=['income', 'expense'])
    amount = FloatField(required=True, min_value=0)
    description = StringField(max_length=500)

    # Recurrence settings
    frequency = StringField(required=True, choices=FREQUENCY_CHOICES)
    interval = IntField(required=True, default=1, min_value=1)  # Every X days/weeks/months
    start_date = DateTimeField(required=True)
    end_date = DateTimeField()  # Optional, None means indefinite
    next_occurrence = DateTimeField(required=True)

    # Status
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    last_generated = DateTimeField()  # Last time a transaction was auto-created

    meta = {
        'collection': 'recurring_transactions',
        'indexes': [
            'user',
            'category',
            'type',
            'is_active',
            'next_occurrence',
            '-created_at'
        ]
    }

    def calculate_next_occurrence(self, from_date=None):
        """Calculate the next occurrence date based on frequency and interval"""
        base_date = from_date or self.next_occurrence or self.start_date

        if self.frequency == 'daily':
            return base_date + timedelta(days=self.interval)
        elif self.frequency == 'weekly':
            return base_date + timedelta(weeks=self.interval)
        elif self.frequency == 'monthly':
            return base_date + relativedelta(months=self.interval)
        elif self.frequency == 'yearly':
            return base_date + relativedelta(years=self.interval)

        return base_date

    def should_generate_transaction(self):
        """Check if it's time to generate a new transaction"""
        if not self.is_active:
            return False

        now = datetime.utcnow()

        # Check if past end date
        if self.end_date and now > self.end_date:
            return False

        # Check if next occurrence has arrived
        return now >= self.next_occurrence

    def generate_transaction(self):
        """Create a new transaction based on this recurring transaction"""
        from transactions.models import Transaction

        transaction = Transaction(
            user=self.user,
            category=self.category,
            type=self.type,
            amount=self.amount,
            description=self.description,
            date=self.next_occurrence
        )
        transaction.save()

        # Update next occurrence
        self.last_generated = datetime.utcnow()
        self.next_occurrence = self.calculate_next_occurrence()
        self.updated_at = datetime.utcnow()
        self.save()

        return transaction

    def to_dict(self):
        """Convert recurring transaction to dictionary"""
        return {
            'id': str(self.id),
            'type': self.type,
            'amount': self.amount,
            'description': self.description,
            'frequency': self.frequency,
            'interval': self.interval,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'next_occurrence': self.next_occurrence.isoformat() if self.next_occurrence else None,
            'is_active': self.is_active,
            'category': {
                'id': str(self.category.id),
                'name': self.category.name,
                'name_translations': self.category.name_translations or {},
                'icon': self.category.icon,
                'color': self.category.color,
            } if self.category else None,
            'last_generated': self.last_generated.isoformat() if self.last_generated else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __str__(self):
        return f"{self.frequency.upper()} {self.type}: {self.amount} - {self.description[:30]}"
