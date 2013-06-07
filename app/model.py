#!/bin/env python

# Ignore dev differnces for Google App Engine (GAE)
# pylint: disable=R0903,W0232

"""Models for the PostPyCon Video Voting Site"""


from google.appengine.ext import db


class Event(db.Model):
    """The PostPyCon Local Event"""

    date = db.DateProperty(indexed=True)
    created = db.DateTimeProperty()
    title = db.StringProperty()
    url = db.StringProperty()
    body = db.TextProperty()
    locked = db.BooleanProperty(default=False, indexed=True)
