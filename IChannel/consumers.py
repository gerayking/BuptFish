import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.layers import get_channel_layer
from django.http import HttpRequest


class Chatting(AsyncJsonWebsocketConsumer):
    chats = dict()

    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        # 加入聊天室
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        try:
            Chatting.chats[self.group_name].add(self)
        except:
            Chatting.chats[self.group_name] = set([self])
        await self.accept()

    async def disconnect(self, close_code):
        # 离开聊天室
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        Chatting.chats[self.group_name].remove(self)
        await self.close()

    # 通过WebSocket，接收数据
    async def receive_json(self, message, **kwargs):
        text_data_json = message
        from_user = text_data_json['fromuser']
        to_user = text_data_json['touser']
        message = text_data_json['message']
        lenth = len(Chatting.chats[self.group_name])
        if lenth == 2:
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'fromuser': from_user,
                    'touser': to_user,
                }
            )
        else:
            await self.channel_layer.group_send(
                to_user,
                {
                    "type": "push.message",
                    "event": {
                        'message': message,
                        'group': self.group_name
                    }

                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['fromuser'] + ':' + event['message']
        print('返回')
        # 通过WebSocket发送
        await self.send(text_data=json.dumps({
            'from_user': event['fromuser'],
            'to_user': event['touser'],
            'message': message
        }))


# 推送consumer
class PushConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['username']
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        # print(PushConsumer.chats)

    async def push_message(self, event):
        print(event)
        await self.send(text_data=json.dumps({
            "event": event['event']
        }))


def push(request: HttpRequest):
    to_user = request.POST['to_user']
    content = request.POST['content']
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        to_user,
        {
            "type": "push.message",
            "event": content
        }
    )
