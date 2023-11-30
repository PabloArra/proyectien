from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('publicar.urls')),
    path('usuarios/',include('usuarios.urls')),
    path('usuarios/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

