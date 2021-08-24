from django.contrib import admin
from django.urls import path, include
from mainapp import views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.index),
    path('api/', include('mainapp.api.urls'))
]
