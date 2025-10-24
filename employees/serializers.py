from rest_framework import serializers
from .repositories import repository


class EmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def validate_email(self, value):
        if repository.email_exists(value):
            raise serializers.ValidationError("An employee with this email already exists")
        return value

