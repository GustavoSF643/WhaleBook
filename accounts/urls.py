from django.urls import path

from accounts.views import (AddBookView, AddUserFriendView, CreateAcountView,
                            CustomizedTokenObtainPairView, ListUsersView,
                            RetrieveUpdateUserView)

urlpatterns = [
    path('accounts/', CreateAcountView.as_view()),
    path('login/', CustomizedTokenObtainPairView.as_view()),
    path('users/', ListUsersView.as_view()),
    path('users/<int:user_id>/', RetrieveUpdateUserView.as_view()),
    path('users/<int:friend_id>/add', AddUserFriendView.as_view()),
    path('users/<int:user_book_id>/', AddBookView.as_view())
]
