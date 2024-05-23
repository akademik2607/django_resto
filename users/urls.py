from .views import auth
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('auth/', auth, name='auth'),
]
