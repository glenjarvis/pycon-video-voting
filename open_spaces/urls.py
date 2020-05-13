"""OpenSpaces URLs"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.open_spaces_board, name='open-spaces-board'),
    path('space/<int:space_id>/', views.space, name='open-spaces-space'),
    path('new_space/', views.new_space, name='new_open-space'),
]
