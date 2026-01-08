from rest_framework import serializers
from .models import Goal
from datetime import datetime


class GoalSerializer(serializers.Serializer):
    """Serializer for Goal model"""
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=200, required=True)
    target_amount = serializers.FloatField(required=True, min_value=0)
    current_amount = serializers.FloatField(default=0, min_value=0)
    deadline = serializers.DateTimeField(required=False, allow_null=True)
    status = serializers.ChoiceField(
        choices=['active', 'achieved', 'cancelled'],
        default='active'
    )
    description = serializers.CharField(max_length=1000, required=False, allow_blank=True)
    progress_percentage = serializers.SerializerMethodField(read_only=True)
    remaining_amount = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def get_progress_percentage(self, obj):
        """Get progress percentage"""
        return obj.get_progress_percentage()

    def get_remaining_amount(self, obj):
        """Get remaining amount"""
        return obj.get_remaining_amount()

    def create(self, validated_data):
        """Create new goal"""
        user = self.context['request'].user_obj
        goal = Goal(user=user, **validated_data)
        goal.save()
        return goal

    def update(self, instance, validated_data):
        """Update goal"""
        instance.name = validated_data.get('name', instance.name)
        instance.target_amount = validated_data.get('target_amount', instance.target_amount)
        instance.current_amount = validated_data.get('current_amount', instance.current_amount)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.status = validated_data.get('status', instance.status)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_at = datetime.utcnow()
        instance.save()
        return instance

    def to_representation(self, instance):
        """Convert to dictionary"""
        return instance.to_dict()
