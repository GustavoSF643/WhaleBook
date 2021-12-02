from accounts.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

class BookViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="user",
            password="12345678",
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))

    def test_user_can_list_books(self):
        response = self.client.get("/api/books/?q=''")

        self.assertEqual(response.status_code, 200)

    def test_user_can_access_a_specific_book(self):
        books = self.client.get("/api/books/?q=''").json()
        
        book = books[0]
        book_url = book['selfLink']

        response = self.client.get(book_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(book['volumeInfo']['title'], response.json()['volumeInfo']['title'])