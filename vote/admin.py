"""Voting App for upvoting Talks to view"""

from django.contrib import admin

from vote.models import Event, Talk

class EventAdmin(admin.ModelAdmin):
    """Default EventAdmin

    Please note that this has been converted to Django for a single event. We
    have deprecated using this event and will not currently being using this
    Admin.
    """
admin.site.register(Event, EventAdmin)

class TalkAdmin(admin.ModelAdmin):
    """Admin for PyCon Video Talks

    Useful for entering talk data, updating scores and marking videos s
    "Viewed" so they no longer show on the list.
    """
    list_display = ('score', 'title', 'viewed')
admin.site.register(Talk, TalkAdmin)
