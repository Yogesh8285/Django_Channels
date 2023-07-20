from django.urls import path
from . import consumers

webscocket_urlpattern = [
path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
path('ws/ac/', consumers.MyASyncConsumer.as_asgi()),


]