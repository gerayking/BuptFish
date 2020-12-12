from django.conf.urls import url
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<group_name>[a-z_0-9]+)$', consumers.Chatting.as_asgi()),  # consumers.Chatting 是该路由的消费者
    url(r'^push/(?P<username>[0-9a-z]+)/$', consumers.PushConsumer.as_asgi()),
]
