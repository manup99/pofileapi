from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import UserProfile
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name=serializers.CharField(max_length=20)
class ProfileSerializer(serializers.ModelSerializer):
    """Serialize a user profile object"""
    class Meta:
        model=UserProfile
        fields=('name','id','email','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    """Overwrite create function"""
    def create(self,validated_data):
        user=UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
    def update(self,instance,validated_data):
        """Handling updated user"""
        if 'password' in validated_data:
            password=validated_data['password']
            instance.set_password(password)
        return super().update(instance,validated_data)

