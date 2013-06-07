#!/bin/env python

# Ignore dev differnces for Google App Engine (GAE)
# pylint: disable=F0401, F0401, W0232, E1101, R0903

"""Controller for the PostPyCon Video Voting Site

Main entry point is controller.application
(where controller is this file).
"""

import datetime
import os

import jinja2
import webapp2

from app.model import Event

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
    extensions=['jinja2.ext.autoescape'])


class MainPage(webapp2.RequestHandler):

    """Main Page controller for initial get"""

    def get(self):

        """Initial page load (index.html) for main controller"""

        event_q = Event.all()
        event_q.filter("date > ", datetime.date.today())

        template_values = {
            'events': event_q,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

# This non-constant name is okay; pylint: disable=C0103
application = webapp2.WSGIApplication([('/', MainPage)], debug=True)
