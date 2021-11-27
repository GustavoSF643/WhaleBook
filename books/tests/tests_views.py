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
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + refresh.access_token)

    def user_can_list_books(self):
        response = self.client.get('/api/books/')

        self.assertEqual(response.status_code, 200)

    def user_can_list_books_by_category(self):
        category = 'Music'
        response = self.client.get(f'/api/books/?category={category}')

        self.assertEqual(response.status_code, 200)

        for book in response.json():
            for book_category in book['categories']:
                self.assertEqual(bool(category in book_category), True)

    def user_can_list_books_by_title(self):
        title = 'Music'
        response = self.client.get(f'/api/books/?title={title}')

        self.assertEqual(response.status_code, 200)

        for book in response.json():
            book_info = book['volumeInfo']
            self.assertEqual(bool(title in book_info['title']), True)

    def user_can_access_a_specific_book(self):
        books = self.client.get('/api/books/').json()
        book = books[0]
        book_url = book['book_url']

        response = self.client.get(book_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(book['volumeInfo']['title'], response.json()['volumeInfo']['title'])