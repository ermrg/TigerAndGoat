"""tag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('', index),
    path('multiplayer-offline', multiplayer_offline, name="multiplayer_offline"),
    path('multiplayer-online', multiplayer_online, name="multiplayer_online"),
    path('create-online-game', create_online_game, name="create_online_game"),
    path('join-online-game', join_online_game, name="join_online_game"),
    path('game-setup', setup_game, name="setup_game"),
    path('game-setup/<int:code>', setup_game, name="setup_game"),
]
