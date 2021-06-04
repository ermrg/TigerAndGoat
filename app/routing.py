# from channels.routing import route, route_class
# from channels.staticfiles import StaticFilesConsumer
from django.urls import path
# routes defined for channel calls
# this is similar to the Django urls, but specifically for Channels
from .consumers import ConnectConsumer, PlayConsumer

channel_routing = [
    path('ws/game-setup/<code>', ConnectConsumer.as_asgi()),
    path('ws/play/<code>', PlayConsumer.as_asgi())
]