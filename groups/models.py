from django.db import models

class Group(models.Model):
    leader = models.ForeignKey('accounts.User', on_delete=models.PROTECT, related_name='leader')
    name = models.CharField(max_length=150)

    users = models.ManyToManyField('accounts.User', through='groups.GroupUser')

class GroupUser(models.Model):
    group = models.ForeignKey('groups.Group', on_delete=models.PROTECT)
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    is_admin = models.BooleanField(default=False)

class JoinGroupRequest(models.Model):
    group = models.ForeignKey('groups.Group', on_delete=models.PROTECT)
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT) 