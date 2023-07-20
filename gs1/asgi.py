
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import Myapp.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs1.settings')

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket': URLRouter(
        Myapp.routing.webscocket_urlpattern
    ),
})
