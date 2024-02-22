from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.sign_up, name='register'),
    path('login', views.user_login, name='login'),
]