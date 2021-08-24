from django.db import models
from django.contrib.auth.models import AbstractUser


class DiaryUser(AbstractUser):
    is_active = models.BooleanField(default=False)


class UserSettings(models.Model):
    user = models.ForeignKey(
        DiaryUser,
        on_delete=models.CASCADE,
        related_name='settings'
    )
    private = models.BooleanField(default=False)
    notifications = models.BooleanField(default=False)
    activation_key = models.CharField(max_length=128, null=True)
    updated = models.DateTimeField(auto_now=True)


class UserWhiteList(models.Model):
    user = models.ForeignKey(
        DiaryUser,
        on_delete=models.CASCADE,
    )
    white_list_user = models.ForeignKey(
        DiaryUser,
        on_delete=models.CASCADE,
        related_name='white_list_users'
    )
