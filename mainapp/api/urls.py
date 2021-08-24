from django.urls import path
from .views import TestApiView

urlpatterns = [
    path('test-api/', TestApiView.as_view(), name='test'),
]