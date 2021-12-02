from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import status
from books.models import BookReview
from books.serializers import BooksSerializer, ReviewSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BooksView(APIView):
    def get(self, request):
        books_request_url = f"https://www.googleapis.com/books/v1/volumes"

        for count, param in enumerate(request.query_params.items()):
            if count == 0:
                books_request_url += f"?{param[0]}={param[1]}"
            else:
                books_request_url += f"&{param[0]}={param[1]}"

        response = requests.get(books_request_url)

        if response.status_code != 200:
            return Response(response.json(), status=response.status_code)

        try:
            books = response.json()['items']
        except KeyError:
            return Response(response.json(), status=response.status_code)

        for book in books:
            book['selfLink'] = f"/api/books/{book['id']}/"
            book_reviews = BookReview.objects.filter(book_id=book['id'])
            book_average_rating = 5
            if len(book_reviews) > 0:
                book_total_rating = 0
                for book_review in book_reviews:
                    book_total_rating += book_review.stars
                
                book_average_rating = book_total_rating / len(book_reviews)
            book['volumeInfo']['averageRating'] = book_average_rating

        serializer = BooksSerializer(data=books, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class BookRetrieveView(APIView):
    def get(self, request, book_id):
        book_request_url = f"https://www.googleapis.com/books/v1/volumes/{book_id}"
        response = requests.get(book_request_url)

        if response.status_code != 200:
            return Response(response.json(), status=response.status_code)

        book = response.json()
        book_reviews = BookReview.objects.filter(book_id=book_id)
        book_average_rating = 5
        if len(book_reviews) > 0:
            book_total_rating = 0
            for book_review in book_reviews:
                book_total_rating += book_review.stars
            
            book_average_rating = book_total_rating / len(book_reviews)

        book['volumeInfo']['averageRating'] = book_average_rating

        serializer = BooksSerializer(data=book)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ReviewView(generics.ListCreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def filter_queryset(self, queryset):
        queryset = self.queryset.filter(book_id=self.kwargs.get('book_id'))

        return super().filter_queryset(queryset)

class ReviewRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookReview.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_url_kwarg = 'review_id'


