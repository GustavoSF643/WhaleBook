from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class UserFriend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='friends')
    friends = models.ForeignKey(User, on_delete=models.SET_NULL)
