from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    friends = models.ManyToManyField('accounts.User')


class UserBooks(models.Model):
    book_url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    total_pages = models.IntegerField()
    current_page = models.IntegerField()
    is_favorite = models.BooleanField(default=True)
    is_reading = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='books')
