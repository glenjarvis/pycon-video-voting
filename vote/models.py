from django.db import models

"""Models for the Video Voting"""

class Event(models.Model):
    """The PostPyCon Local Event"""

    date = models.DateField()
    created = models.DateField()
    title = models.CharField(max_length=120)
    url = models.URLField()
    body = models.TextField()
    locked = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Talk(models.Model):
    """The Talk for voting"""

    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
    )
    level = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=99)
    url = models.URLField()
    video = models.URLField()
    score = models.IntegerField(default=0)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
