from django.contrib import admin
from django.urls import path, include
import chat.views as views

urlpatterns = [
    path('', views.lobby, name='lobby_view'),
]