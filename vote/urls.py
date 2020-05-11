"""Vote URLs"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.vote_board, name='index'),
    path('vote_board/', views.vote_board, name='vote-board'),
    path('vote/<int:talk_id>/', views.vote, name='vote'),
]
