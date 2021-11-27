from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import User, UserBooks
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'is_staff', 'is_superuser', 'is_active']
    
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class FriendUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    is_active = serializers.BooleanField()


class UserBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBooks
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):
    friends = FriendUserSerializer(many=True)
    books = UserBooksSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'is_superuser',
                  'friends', 'books']
        
        extra_kwargs = {
            'friends': {'read_only': True},
            'books': {'read_only': True}
        }


class CustomizedTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user'] = user.username
        return token


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'is_superuser', 'is_active']
