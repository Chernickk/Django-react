from django.db import models
from django.conf import settings


class DayNote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    note_date = models.DateField(null=False, db_index=True)
    text = models.TextField(null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


class DayToDoList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='daily_todo_lists'
    )
    name = models.CharField(max_length=128, null=True)
    list_date = models.DateField(null=False, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


class DayToDoPoints(models.Model):
    todo_list = models.ForeignKey(
        DayToDoList,
        on_delete=models.CASCADE,
        related_name='points'
    )
    text = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    order_num = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)


class GlobalToDoList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='global_todo_lists'
    )
    name = models.CharField(max_length=128)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


class GlobalToDoPoints(models.Model):
    todo_list = models.ForeignKey(
        GlobalToDoList,
        on_delete=models.CASCADE,
        related_name='points'
    )
    text = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    order_num = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
