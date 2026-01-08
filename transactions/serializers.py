from rest_framework import serializers
from .models import Transaction
from categories.models import Category
from datetime import datetime


class TransactionSerializer(serializers.Serializer):
    """Serializer for Transaction model"""
    id = serializers.CharField(read_only=True)
    type = serializers.ChoiceField(choices=['income', 'expense'], required=True)
    amount = serializers.FloatField(required=True, min_value=0)
    description = serializers.CharField(max_length=500, required=False, allow_blank=True)
    date = serializers.DateTimeField(required=False)
    category_id = serializers.CharField(write_only=True, required=True)
    category = serializers.SerializerMethodField(read_only=True)
    tags = serializers.ListField(child=serializers.CharField(max_length=50), required=False)
    created_at = serializers.DateTimeField(read_only=True)

    def get_category(self, obj):
        """Get category data"""
        if obj.category:
            return {
                'id': str(obj.category.id),
                'name': obj.category.name,
                'icon': obj.category.icon,
                'color': obj.category.color,
            }
        return None

    def validate_category_id(self, value):
        """Validate category exists and belongs to user or is accessible"""
        user = self.context['request'].user_obj
        # Check if category exists and belongs to user
        category = Category.objects(id=value, user=user).first()
        if not category:
            raise serializers.ValidationError("Категория не найдена или недоступна.")
        return value

    def create(self, validated_data):
        """Create new transaction"""
        user = self.context['request'].user_obj
        category_id = validated_data.pop('category_id')
        category = Category.objects(id=category_id).first()

        if 'date' not in validated_data:
            validated_data['date'] = datetime.utcnow()

        transaction = Transaction(
            user=user,
            category=category,
            **validated_data
        )
        transaction.save()
        return transaction

    def update(self, instance, validated_data):
        """Update transaction"""
        if 'category_id' in validated_data:
            category_id = validated_data.pop('category_id')
            category = Category.objects(id=category_id).first()
            instance.category = category

        instance.type = validated_data.get('type', instance.type)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.updated_at = datetime.utcnow()
        instance.save()
        return instance

    def to_representation(self, instance):
        """Convert to dictionary"""
        return instance.to_dict()
