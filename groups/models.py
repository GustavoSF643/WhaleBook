from django.db import models
from django.db.models.deletion import CASCADE, PROTECT


class Group(models.Model):
    leader = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='leader')
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=511, null=True)

    users = models.ManyToManyField('accounts.User', through='groups.GroupUser')

class GroupUser(models.Model):
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

class JoinGroupRequest(models.Model):
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='requests')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE) 

class GroupGoals(models.Model):
    owner = models.ForeignKey('accounts.User', on_delete=PROTECT, related_name='owner')
    group = models.ForeignKey('groups.Group', on_delete=CASCADE)
    book_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    image_url = models.CharField(max_length=255)
    deadline = models.DateField(null=True)
    description = models.CharField(max_length=511, null=True)

    members = models.ManyToManyField('accounts.User', through='groups.GroupGoalsUsers')

class GroupGoalsUsers(models.Model):
    group_goal = models.ForeignKey('groups.GroupGoals', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
