from django.http import HttpResponse
from django.shortcuts import render


def multiplayer_offline(request):
    return render(request, 'app/offline_board.html')


def multiplayer_online(request):
    return render(request, 'app/online_board.html')


def index(request):
    return render(request, 'app/home.html')
