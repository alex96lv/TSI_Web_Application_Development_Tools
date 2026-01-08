from rest_framework import serializers
from .models import Budget
from categories.models import Category
from datetime import datetime


class BudgetSerializer(serializers.Serializer):
    """Serializer for Budget model"""
    id = serializers.CharField(read_only=True)
    limit_amount = serializers.FloatField(required=True, min_value=0)
    period = serializers.ChoiceField(choices=['weekly', 'monthly'], default='monthly')
    is_active = serializers.BooleanField(default=True)
    category_id = serializers.CharField(write_only=True, required=True)
    category = serializers.SerializerMethodField(read_only=True)
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
        """Validate category exists and belongs to user"""
        user = self.context['request'].user_obj
        category = Category.objects(id=value, user=user).first()
        if not category:
            raise serializers.ValidationError("Категория не найдена.")
        if category.type != 'expense':
            raise serializers.ValidationError("Бюджет можно создать только для категорий расходов.")
        return value

    def create(self, validated_data):
        """Create new budget"""
        user = self.context['request'].user_obj
        category_id = validated_data.pop('category_id')
        category = Category.objects(id=category_id).first()

        budget = Budget(user=user, category=category, **validated_data)
        budget.save()
        return budget

    def update(self, instance, validated_data):
        """Update budget"""
        if 'category_id' in validated_data:
            category_id = validated_data.pop('category_id')
            category = Category.objects(id=category_id).first()
            instance.category = category

        instance.limit_amount = validated_data.get('limit_amount', instance.limit_amount)
        instance.period = validated_data.get('period', instance.period)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.updated_at = datetime.utcnow()
        instance.save()
        return instance

    def to_representation(self, instance):
        """Convert to dictionary"""
        return instance.to_dict()
