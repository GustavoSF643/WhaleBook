from django.urls import path
from .views import BooksView, BookRetrieveView, ReviewRetrieveView, ReviewView

urlpatterns = [
  path('books/', BooksView.as_view()),
  path('books/<str:book_id>/', BookRetrieveView.as_view()),
  path('books/<str:book_id>/reviews/', ReviewView.as_view()),
  path('books/<str:book_id>/reviews/<int:review_id>/', ReviewRetrieveView.as_view()),
]