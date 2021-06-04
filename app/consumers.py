import json
from time import sleep

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from app.helper import get_game_by_code


class ConnectConsumer(WebsocketConsumer):
    def connect(self):
        code = self.scope['url_route']['kwargs']['code']
        self.room_name = code
        self.room_group_name = 'room_' + str(self.room_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'join_user',
                'payload': text_data
            }
        )

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def join_user(self, event):
        data = event['payload']
        data = json.loads(data)
        data = data['data']
        if data['operation_type'] == 'join_user':
            user_id = data['user_id']
            code = data['code']
            game = get_game_by_code(code)

            if game.creator_id != int(user_id):
                game.opponent_id = user_id
                game.save()

            data = {
                'creator_name': game.creator.first_name,
                'creator_role': game.creator_role,
                'creator_id': game.creator_id,
                'opponent_name': game.opponent.first_name if game.opponent else '',
                'opponent_role': game.opponent_role,
                'opponent_id': game.opponent_id,
                'game_code': game.code,
            }
            self.send(text_data=json.dumps({
                'payload': data
            }))
        else:
            self.send(text_data=json.dumps({
                'payload': 'start'
            }))


class PlayConsumer(WebsocketConsumer):
    def connect(self):
        code = self.scope['url_route']['kwargs']['code']
        self.room_name = code
        self.room_group_name = 'room_' + str(self.room_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        game = get_game_by_code(code)
        game.has_started = 1
        game.save()
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'movement',
                'payload': text_data
            }
        )

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def movement(self, event):
        data = event['payload']
        data = json.loads(data)
        data = data['data']
        if data['operation_type'] == 'movement':
            self.send(text_data=json.dumps({
                'payload': data
            }))
        elif data['operation_type'] == 'complete':
            self.send(text_data=json.dumps({
                'payload': data
            }))
