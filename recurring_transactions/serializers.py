from rest_framework import serializers
from .models import RecurringTransaction
from datetime import datetime


class RecurringTransactionSerializer(serializers.Serializer):
    """Serializer for RecurringTransaction model"""

    id = serializers.CharField(read_only=True)
    type = serializers.ChoiceField(choices=['income', 'expense'], required=True)
    category = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True, min_value=0)
    description = serializers.CharField(required=False, allow_blank=True, max_length=500)
    frequency = serializers.ChoiceField(
        choices=['daily', 'weekly', 'monthly', 'yearly'],
        required=True
    )
    interval = serializers.IntegerField(min_value=1, default=1)
    start_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=False, allow_null=True)
    next_occurrence = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(default=True)
    last_generated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def validate_category(self, value):
        """Validate category exists"""
        from categories.models import Category
        try:
            category = Category.objects(id=value).first()
            if not category:
                raise serializers.ValidationError("Категория не найдена")
            return category
        except:
            raise serializers.ValidationError("Некорректный ID категории")

    def validate(self, data):
        """Validate the entire recurring transaction"""
        # Check end_date is after start_date
        if data.get('end_date') and data.get('start_date'):
            if data['end_date'] <= data['start_date']:
                raise serializers.ValidationError({
                    'end_date': 'Дата окончания должна быть позже даты начала'
                })
        return data

    def create(self, validated_data):
        """Create a new recurring transaction"""
        user = self.context['request'].user_obj

        recurring_transaction = RecurringTransaction(
            user=user,
            category=validated_data['category'],
            type=validated_data['type'],
            amount=validated_data['amount'],
            description=validated_data.get('description', ''),
            frequency=validated_data['frequency'],
            interval=validated_data['interval'],
            start_date=validated_data['start_date'],
            end_date=validated_data.get('end_date'),
            next_occurrence=validated_data['start_date'],
            is_active=validated_data.get('is_active', True)
        )
        recurring_transaction.save()
        return recurring_transaction

    def update(self, instance, validated_data):
        """Update an existing recurring transaction"""
        instance.type = validated_data.get('type', instance.type)
        instance.category = validated_data.get('category', instance.category)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.description = validated_data.get('description', instance.description)
        instance.frequency = validated_data.get('frequency', instance.frequency)
        instance.interval = validated_data.get('interval', instance.interval)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.updated_at = datetime.utcnow()

        # Recalculate next occurrence if frequency or interval changed
        if 'frequency' in validated_data or 'interval' in validated_data:
            instance.next_occurrence = instance.calculate_next_occurrence()

        instance.save()
        return instance
