from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import User, UserBooks


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
        extra_kwargs = {
            'id': {'read_only': True},
            'email': {'required': True},
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

    def create(self, validated_data):
        return UserBooks.objects.create(**validated_data, user=self.context['resquest'].user)
    
    def update(self, instance, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().update(instance, validated_data)


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


class UserBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBooks
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class UserReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book_id = serializers.CharField()
    stars = serializers.IntegerField()
    review = serializers.CharField()
