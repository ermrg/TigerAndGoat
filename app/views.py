from django.http import HttpResponse
from django.shortcuts import render


def multiplayer_offline(request):
    return render(request, 'app/offline_board.html')


def create_online_game(request):
    # create user here
    return render(request, 'app/create_online_game.html')


def invite_friends(request):
    # create game here
    return render(request, 'app/invite_friend.html')


def multiplayer_online(request):
    return render(request, 'app/online_board.html')


def index(request):
    return render(request, 'app/home.html')
