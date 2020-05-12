from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name=serializers.CharField(max_length=20)

