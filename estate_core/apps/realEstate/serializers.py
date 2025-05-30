from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    """
    부동산 매물 시리얼라이저
    """
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'property_type', 'price',
            'address', 'area', 'rooms', 'bathrooms', 'owner',
            'owner_username', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at'] 