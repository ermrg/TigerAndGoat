from django.conf import settings # import the settings file


def running_ip(request):
    return {'RUNNING_IP': settings.RUNNING_IP}
