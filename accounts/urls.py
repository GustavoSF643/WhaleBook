from django.urls import path

from accounts.views import (FriendsRequestsView, ListAddBookView, AddRemoveUserFriendView, CreateAcountView, RetrieveUpdateDeleteUserBooks,
                            CustomizedTokenObtainPairView, ListUsersView,
                            RetrieveUpdateUserView, FriendsView, UserRetrieveView, 
                            UserReviewsView, FriendsRequestRetrieveView)

urlpatterns = [
    path('accounts/', CreateAcountView.as_view()),
    path('login/', CustomizedTokenObtainPairView.as_view()),
    path('users/', ListUsersView.as_view()),
    path('users/<int:user_id>/', RetrieveUpdateUserView.as_view()),
    path('user/', UserRetrieveView.as_view()),
    path('user/friends/', FriendsView.as_view()),
    path('user/friends/requests/', FriendsRequestsView.as_view()),
    path('user/friends/requests/<int:friend_id>/', FriendsRequestRetrieveView.as_view()),
    path('user/friends/<int:friend_id>/', AddRemoveUserFriendView.as_view()),
    path('user/books/', ListAddBookView.as_view()),
    path('user/books/<int:book_id>/', RetrieveUpdateDeleteUserBooks.as_view()),
    path('user/reviews/', UserReviewsView.as_view()),
]
