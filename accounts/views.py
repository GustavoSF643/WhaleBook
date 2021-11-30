from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import User, UserBooks
from accounts.serializers import (CreateUserSerializer,
                                  CustomizedTokenPairSerializer, UserBooksSerializer,
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
    permission_classes = [IsAuthenticatedOrReadOnly]

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


class AddRemoveUserFriendView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, friend_id):
        user = request.user
        friend = User.objects.get(id=friend_id)
        user.friends.add(friend)
        serializer = UserDataSerializer(user)
        return Response(serializer.data)
    
    def delete(self, request, friend_id):
        user = request.user
        user.friends.remove(friend_id)
        serializer = UserDataSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class ListAddBookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = UserBooks.objects.all()
    serializer_class = UserBooksSerializer

    def get_queryset(self):
        self.queryset = self.queryset.filter(user=self.request.user.id)
        return super().get_queryset()
    
    def create(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user.id).filter(title=request.data['title'])
        if queryset:
            return Response({
                'error': 'Book already added'
            }, status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class RetrieveUpdateDeleteUserBooks(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = UserBooks.objects.all()
    serializer_class = UserBooksSerializer
    
    lookup_url_kwarg = 'book_id'
