from django.db import models

"""Models for the Video OpenSpaces"""

class OpenSpace(models.Model):
    """PyCon Online Open Spaces"""

    topic = models.CharField(max_length=120)
    host = models.CharField(max_length=120, help_text="Person who will host")
    meeting_type = models.CharField(max_length=120)
    # Meeting Type: Zoom, Jitsu, Hangouts, Other
    invitation = models.TextField()

    def __str__(self):
        return self.topic

