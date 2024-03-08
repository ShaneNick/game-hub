"""
ASGI config for game_hub project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import tic_tac_toe.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_hub.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Handle HTTP requests with Django's ASGI application
    # Define the WebSocket protocol path here
    "websocket": AuthMiddlewareStack(
        URLRouter(
            tic_tac_toe.routing.websocket_urlpatterns  # Use your app's WebSocket URL routing
        )
    ),
})

