from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import status
from books.serializers import BooksSerializer

class BooksView(APIView):
    def get(self, request):
        books_request_url = f"https://www.googleapis.com/books/v1/volumes"

        for count, param in enumerate(request.query_params.items()):
            if count == 0:
                books_request_url += f"?{param[0]}={param[1]}"
            else:
                books_request_url += f"&{param[0]}={param[1]}"

        api_request = requests.get(books_request_url).json()

        try:
            books = api_request['items']
        except KeyError:
            return Response(api_request['error'], status=status.HTTP_400_BAD_REQUEST)

        for book in books:
            book['selfLink'] = f"/api/books/{book['id']}/"

        serializer = BooksSerializer(data=books, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class BookRetrieveView(APIView):
    def get(self, request, book_id):
        book_request_url = f"https://www.googleapis.com/books/v1/volumes/{book_id}"
        book = requests.get(book_request_url).json()

        serializer = BooksSerializer(data=book)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)