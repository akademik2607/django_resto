from django.urls import path

from checklist.consumers import Consumer

ws_urlpatterns = [
    path('ws/<role>/', Consumer.as_asgi()),
]

