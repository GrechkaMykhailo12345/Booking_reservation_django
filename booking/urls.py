from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('room/<int:room_id>', views.booking_page, name='booking_page')
]