"""OpenSpaces App for adding OpenSpaces to board"""

from django.contrib import admin

from open_spaces.models import OpenSpace

class OpenSpaceAdmin(admin.ModelAdmin):
    """OpenSpace Admin for Online PyCon BAyPIGgies Event """
admin.site.register(OpenSpace, OpenSpaceAdmin)

