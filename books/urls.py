from django.urls import path
from .views import BooksView, BookRetrieveView

urlpatterns = [
  path('books/', BooksView.as_view()),
  path('books/<str:book_id>/', BookRetrieveView.as_view()),
]