"""PyCon Video Voting Site URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vote.urls')),
    # Removing OpenSpaces for 2020-05 path('open_spaces/', include('open_spaces.urls')),
]
