from django.contrib import admin


from vote.models import Event, Talk

class EventAdmin(admin.ModelAdmin):
        pass
admin.site.register(Event, EventAdmin)

class TalkAdmin(admin.ModelAdmin):
        pass
admin.site.register(Talk, TalkAdmin)
