from django.contrib import admin
from .models import DayToDoList, DayNote, DayToDoPoints, GlobalToDoPoints, GlobalToDoList

admin.site.register(DayNote)
admin.site.register(DayToDoList)
admin.site.register(DayToDoPoints)
admin.site.register(GlobalToDoPoints)
admin.site.register(GlobalToDoList)
