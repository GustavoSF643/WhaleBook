from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    friends = models.ManyToManyField('accounts.User', through='UserFriends')
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class UserFriends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='me')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    is_friend = models.BooleanField(default=False)


class UserBooks(models.Model):
    book_url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    total_pages = models.IntegerField()
    current_page = models.IntegerField(default=0)
    is_favorite = models.BooleanField(default=True)
    is_reading = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='books')
