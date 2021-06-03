import random

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify

from app.helper import get_client_ip, get_user_by_ip, get_user_by_username, get_game_by_code
from app.models import Game


def multiplayer_offline(request):
    return render(request, 'app/offline_board.html')


def create_online_game(request):
    # create user here
    return render(request, 'app/create_online_game.html')


def join_online_game(request):
    # create user here
    return render(request, 'app/join_online_game.html')


def invite_friends(request, code=None):
    if request.method == 'POST':
        data = request.POST
        ip = get_client_ip(request)
        user = get_user_by_ip(ip)
        if not user:
            user = User()
            username = slugify(data['name'])
            i = 1
            while get_user_by_username(username):
                username = username + '_' + str(i)
                i = i + 1
            user.username = username
            user.first_name = data['name']
        else:
            user.first_name = data['name']
        user.save()
        if 'code' in data and data['code']:
            game = get_game_by_code(data['code'])
            return render(request, 'app/invite_friend.html', {'game': game, 'user_id': user.id})
        game = Game()
        game.creator = user
        game.creator_role = 'TIGER'
        game.opponent_role = 'GOAT'
        code = random.randint(1111, 9999)
        while get_game_by_code(code):
            code = random.randint(1111, 9999)
        game.code = code
        game.save()
        return render(request, 'app/invite_friend.html', {'game': game, 'user_id': user.id})
    # Opponent

    return render(request, 'app/join_online_game.html', {'code': code})


def multiplayer_online(request, code, user_id):
    game = get_game_by_code(code)
    return render(request, 'app/online_board.html', {'game': game, 'user_id': user_id})


def index(request):
    return render(request, 'app/home.html')
