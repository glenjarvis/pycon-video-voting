"""Vote URLs"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.voting_closed, name='index'),
    path('vote_board/', views.vote_board, name='vote-board'),
    path('vote/<int:talk_id>/', views.vote, name='vote'),
]
