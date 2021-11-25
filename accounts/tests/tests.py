from django.test import TestCase
from accounts.models import User
from rest_framework.test import APITestCase


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = 'user'
        cls.password = '12345678'
        cls.is_staff = True
        cls.is_superuser = True
        cls.is_active = True

        cls.user = User.objects.create_user(
            username=cls.username,
            password=cls.password,
            is_staff=cls.is_staff,
            is_superuser=cls.is_superuser,
            is_active=cls.is_active
        )

    def test_user_has_all_fields(self):
        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.is_staff, self.is_staff)
        self.assertEqual(self.user.is_superuser, self.is_superuser)
        self.assertEqual(self.user.is_active, self.is_active)

        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.username, str)
        self.assertIsInstance(self.user.is_staff, bool)
        self.assertIsInstance(self.user.is_superuser, bool)
        self.assertIsInstance(self.user.is_active, bool)
        self.assertNotIsInstance(self.user.is_active, str)


class UserViewsTest(APITestCase):
    def setUp(self):
        self.admin_user = {
            "username": "machado",
            "password": "123456",
            "is_staff": True,
            "is_superuser": True
        }
        self.login_admin_user = {
            "username": "machado",
            "password": "123456"
        }

        self.ordinary_user_1 = {
            "username": "fpessoa",
            "password": "123456",
            "is_superuser": False,
            "is_staff": True
        }
        self.login_ordinary_user_1 = {
            "username": "fpessoa",
            "password": "123456"
        }

        self.login_admin_user_wrong_password = {
            "username": "machado",
            "password": "36549"
        }
        
        self.login_not_found_user = {
            "username": "saramago",
            "password": "123456"
        }

        self.missing_data_user_1 = {
            "username": "saramago",
            "password": "123456",
            "is_staff": True,
        }

        self.missing_data_user_2 = {
            "username": "lispector",
            'password': "",
            "is_superuser": True,
            "is_staff": True
        }

    def test_create_user(self):
        response = self.client.post('/api/accounts/', self.admin_user)

        self.assertEqual(response.status_code, 201)
        user_from_response = {
            "id": 1,
            "username": "machado",
            "is_staff": True,
            "is_superuser": True,
            "is_active": True
        }
        self.assertEqual(response.json(), user_from_response)
        self.assertIn('id', response.json())

    def test_create_user_aleady_exists_fail(self):

        self.client.post('/api/accounts/', self.admin_user)
        response = self.client.post('/api/accounts/', self.admin_user)

        self.assertDictEqual(response.json(), {"username": [
            "A user with that username already exists."
        ]})
        self.assertEqual(response.status_code, 400)

    def test_create_user_fail(self):
        response = self.client.post('/api/accounts/', self.missing_data_user_1)
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.json(), {
            "is_superuser": ["This field is required"]
        })

        response = self.client.post('/api/accounts/', self.missing_data_user_2)
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.json(), {
            "password": [
                "This field may not be blank."
        ]})

    def test_login_user(self):
        self.client.post('/api/accounts/', self.ordinary_user_1)
        response = self.client.post('/api/login/', self.login_ordinary_user_1)
        self.assertIn('access_token', response.json())
        self.assertEqual(response.status_code, 200)

    def test_login_user_fail(self):
        self.client.post('/api/accounts/', self.admin_user)
        response = self.client.post('/api/login/',
                                    self.login_admin_user_wrong_password)
        
        self.assertDictEqual(response.json(), {
            'error': 'username or password do not match'
        })
        self.assertEqual(response.status_code, 401)

    def test_login_user_not_found_fail(self):
        self.client.post('/api/accounts/', self.admin_user)
        response = self.client.post('/api/login/',
                                    self.login_not_found_user)
        
        self.assertDictEqual(response.json(), {
            'error': 'This user does not exist'
        })
        self.assertEqual(response.status_code, 404)
