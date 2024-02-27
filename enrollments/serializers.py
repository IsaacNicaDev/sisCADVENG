from rest_framework import serializers

from .models import Enrollment



class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ("id", "student_id", "group_id", "created_at", "updated_at")
        read_only_fields = ("created_at",)