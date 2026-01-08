from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    """Serializer for Category model"""
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100, required=True)
    name_translations = serializers.DictField(required=False, default=dict)
    type = serializers.ChoiceField(choices=['income', 'expense'], required=True)
    icon = serializers.CharField(max_length=50, default='⚡')
    color = serializers.CharField(max_length=7, default='#6366f1')
    is_default = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        """Create new category"""
        user = self.context['request'].user_obj
        category = Category(user=user, **validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        """Update category"""
        instance.name = validated_data.get('name', instance.name)
        instance.name_translations = validated_data.get('name_translations', instance.name_translations)
        instance.type = validated_data.get('type', instance.type)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance

    def to_representation(self, instance):
        """Convert to dictionary"""
        return instance.to_dict()
