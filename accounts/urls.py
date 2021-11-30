from django.urls import path

from accounts.views import (ListAddBookView, AddRemoveUserFriendView, CreateAcountView, RetrieveUpdateDeleteUserBooks,
                            CustomizedTokenObtainPairView, ListUsersView,
                            RetrieveUpdateUserView)

urlpatterns = [
    path('accounts/', CreateAcountView.as_view()),
    path('login/', CustomizedTokenObtainPairView.as_view()),
    path('users/', ListUsersView.as_view()),
    path('users/<int:user_id>/', RetrieveUpdateUserView.as_view()),
    path('users/friends/<int:friend_id>/', AddRemoveUserFriendView.as_view()),
    path('users/books/', ListAddBookView.as_view()),
    path('users/books/<int:book_id>/', RetrieveUpdateDeleteUserBooks.as_view())
]
