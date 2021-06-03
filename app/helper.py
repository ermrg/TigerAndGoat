from django.contrib.auth.models import User

from app.models import Profile, Game


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_user_by_ip(ip):
    p = Profile.objects.filter(ip=ip).first()
    if p:
        return p.user
    return None


def get_user_by_username(username):
    return User.objects.filter(username=username).first()


def get_game_by_code(code):
    return Game.objects.filter(code=code).first()
