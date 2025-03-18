from rest_framework import serializers
from ..models import *
class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        fields='__all__'

    def validate_course(self, value):
        """Ensure the provided course exists"""
        if not value:
            raise serializers.ValidationError("Course ID is required")
        return value
