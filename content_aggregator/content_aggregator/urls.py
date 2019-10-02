from django.contrib import admin
from django.urls import path

from main import views as main_views

from .on_startup import on_startup_loader

urlpatterns = [
    path('', main_views.homepage, name='index'),
    path('admin/', admin.site.urls),
]

on_startup_loader() 
