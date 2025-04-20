from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', register, name='register'),
    path('login/', login_view, name='login'),
    path('quiz/', quiz, name='quiz'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('logout/', logout_viewl, name='logout'),
]