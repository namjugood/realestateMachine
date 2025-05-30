from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    사용자 시리얼라이저
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at'] 