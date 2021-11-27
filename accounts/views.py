from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import User
from accounts.serializers import (CreateUserSerializer,
                                  CustomizedTokenPairSerializer,
                                  UserDataSerializer, UserUpdateSerializer)


class CreateAcountView(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CustomizedTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomizedTokenPairSerializer


class ListUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSerializer
    
    def filter_queryset(self, queryset):
        queryset = self.queryset.filter(is_active=True)
        return super().filter_queryset(queryset)


class RetrieveUpdateUserView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    lookup_field = 'pk'
    lookup_url_kwarg = 'user_id'

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser or (request.user.__dict__['id'] == kwargs.get('user_id')):
            return super().update(request, *args, **kwargs)
        else:
            return Response({
                'error': 'You are not allowed to update datas from other users.'
            }, status.HTTP_403_FORBIDDEN)
            
    def filter_queryset(self, queryset):
        queryset = self.queryset.filter(is_active=True)
        return super().filter_queryset(queryset)


class AddUserFriendView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, friend_id):
        user = request.user
        friend = User.objects.get(id=friend_id)
        user.friends.add(friend)
        user.save()
        serializer = UserDataSerializer(user)
        return Response(serializer.data)
        