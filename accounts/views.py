from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import User, UserBooks, UserFriends
from accounts.serializers import (CreateUserSerializer,
                                  CustomizedTokenPairSerializer, FriendRequestSerializer, FriendUserSerializer, UserBooksSerializer,
                                  UserDataSerializer, UserFriendSerializer, UserReviewSerializer, UserUpdateSerializer)


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

class UserRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDataSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class FriendsRequestsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sent_requests = UserFriends.objects.filter(user=request.user.id, is_friend=False)
        received_requests = UserFriends.objects.filter(friend=request.user.id, is_friend=False)

        sent_requests_serializer = UserFriendSerializer(sent_requests, many=True)
        received_requests_serializer = FriendRequestSerializer(received_requests, many=True)

        serialized_requests = {
            "sent_requests": sent_requests_serializer.data,
            "received_requests": received_requests_serializer.data
        }

        return Response(serialized_requests, status=status.HTTP_200_OK)


class FriendsRequestRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, friend_id):
        user = request.user
        if user.id == friend_id:
            return Response({"errors": "You cannot add yourself as a friend"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user.friends.get(id=friend_id)
        except User.DoesNotExist:
            try:
                friend = User.objects.get(id=friend_id)
            except User.DoesNotExist:
                return Response({"errors": "User not found."}, status=status.HTTP_404_NOT_FOUND)
                
            user.friends.add(friend)

            friends_requests = UserFriends.objects.filter(user=request.user.id, is_friend=False)

            serializer = UserFriendSerializer(friends_requests, many=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"errors": "Friend already added."}, status=status.HTTP_409_CONFLICT)

    def delete(self, request, friend_id):
        try:
            from django.db.models import Q
            friend_request = UserFriends.objects.filter(
                Q(user=request.user.id, friend=friend_id) | Q(friend=request.user.id, user=friend_id),
                is_friend=False
            )[0]
        except IndexError:
            return Response({"errors": "Friend not in request list."}, status=status.HTTP_400_BAD_REQUEST)

        friend_request.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FriendsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        from django.db.models import Q
        friends = UserFriends.objects.filter(Q(friend=request.user.id) | Q(user=request.user.id), is_friend=True)

        serializer = UserFriendSerializer(friends, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class AddRemoveUserFriendView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, friend_id):
        user = request.user
        if user.id == friend_id:
            return Response({"errors": "You cannot add yourself as a friend"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            friend = UserFriends.objects.filter(friend=user.id, user=friend_id)[0]
            friend.is_friend = True
            friend.save()

            return Response({"message": "Friend added."}, status=status.HTTP_200_OK)
        except IndexError:
            return Response({"errors": "Friend not in request list."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"errors": "Friend already added."}, status=status.HTTP_409_CONFLICT)
    
    def delete(self, request, friend_id):
        user = request.user
        try:
            user.friends.get(id=friend_id)
        except User.DoesNotExist:
            return Response({"errors": "Friend not found."}, status=status.HTTP_404_NOT_FOUND)

        user.friends.remove(friend_id)
        serializer = UserDataSerializer(user)
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)


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
    
    def get_object(self):
        obj = super().get_object()
        
        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj

class UserReviewsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        reviews = user.reviews
        serializer = UserReviewSerializer(reviews, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

