from django.urls import re_path
from .consumers import stockConsumer

websocket_urlpatterns = [
    re_path(r'ws/stocks/$', stockConsumer.as_asgi()),
]