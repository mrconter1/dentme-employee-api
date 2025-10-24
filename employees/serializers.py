import re
from rest_framework import serializers
from .repositories import repository


class EmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=254)  # RFC 5321 standard maximum

    def _validate_name_field(self, value):
        if not re.match(r"^[a-zA-Z\s\-']+$", value):
            raise serializers.ValidationError("Only letters, spaces, hyphens, and apostrophes are allowed")
        return value

    def validate_first_name(self, value):
        return self._validate_name_field(value)

    def validate_last_name(self, value):
        return self._validate_name_field(value)

    def validate_email(self, value):
        if repository.email_exists(value):
            raise serializers.ValidationError("An employee with this email already exists")
        return value

