from rest_framework import serializers
from models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'is_staff', 'is_superuser', 'is_active']
    
    extra_kwargs = {
        'is_active': {'read_only': True},
        'password': {'write_only': True}
    }


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class FriendUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    is_active = serializers.BooleanField()


class UserDataSerializer(serializers.ModelSerializer):
    friends = FriendUserSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'is_superuser', 'is_active',
                  'friends']
