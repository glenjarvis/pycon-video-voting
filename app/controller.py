#!/bin/env python

# Ignore dev differnces for Google App Engine (GAE)
# pylint: disable=F0401, F0401, W0232, E1101, R0903

"""Controller for the PostPyCon Video Voting Site

Main entry point is controller.application
(where controller is this file).
"""

import csv
import datetime
import os

import jinja2
import webapp2

from app.model import Event, Talk

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
    extensions=['jinja2.ext.autoescape'])


class MainPage(webapp2.RequestHandler):

    """Main Page controller for initial get"""

    def get(self):

        """Initial page load (index.html) for main controller"""

        event_q = Event.all()
        event_q.filter("date >= ", datetime.date.today())

        template_values = {
            'events': event_q,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class DataLoadPage(webapp2.RequestHandler):

    """Data Page controller for initial get"""

    def _string_to_date(self, date_string):
        """Convert standard date format 2013-06-20 to datetime.date"""

        # It's okay this isn't a function (for now); pylint: disable=R0201
        return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

    def get(self):

        """Initial page load (index.html) for main controller"""

        self.response.out.write("<html><body>")

        events = {}
        with open('./app/events.csv', 'r') as event_file_handler:
            self.response.out.write("<p>Loading events...</p>")

            for row in csv.DictReader(event_file_handler):

                if row['locked'] == 'True':
                    row['locked'] = True
                else:
                    row['locked'] = False

                row['date'] = self._string_to_date(row['date'])
                row['created'] = datetime.datetime.now()

                # This "kw magic" is actually valid; pylint: disable=W0142
                events[row['date']] = Event(**row)
                events[row['date']].put()

        with open('./app/pycon_data.csv', 'r') as talk_file_handler:
            self.response.out.write("<p>Loading talks...</p>")

            for row in csv.DictReader(talk_file_handler):

                if row['url'] == 'url':
                    continue

                event_date = self._string_to_date(row['event'])
                event = events[event_date]

                row['event'] = event
                if not row['video']:
                    del row['video']

                # This "kw magic" is actually valid; pylint: disable=W0142
                Talk(**row).put()

        self.response.out.write("<p>Done...</p>")
        self.response.out.write("</body></html>")


class VoteBoardPage(webapp2.RequestHandler):
    """Vote board page for a particular event"""

    def get(self, event_key):
        """Display vote board for event given by event_key"""

        this_event = Event.get(event_key)
        talk_q = Talk.all()
        talk_q.filter("event = ", this_event)
        talk_q.filter("viewed =", False)
        talk_q.order('-score')

        template_values = {
            'current_event': this_event,
            'redirect_link':  "/vote_board/%s" % event_key,
            'talks': talk_q
        }

        template = JINJA_ENVIRONMENT.get_template('vote_board.html')
        self.response.write(template.render(template_values))


class VotePage(webapp2.RequestHandler):

    """Page to process vote requests"""

    def post(self, talk_key):
        """Receive vote request and event to redirect to"""

        talk = Talk.get(talk_key)
        talk.score = talk.score + 1
        talk.put()

        self.redirect(self.request.get('redirect_link'))

class ViewedPage(webapp2.RequestHandler):

    """Page to process 'video already viewed' requests"""

    def post(self, talk_key):
        """Receive 'viewed' request and event to redirect to"""

        talk = Talk.get(talk_key)
        talk.viewed = True
        talk.put()

        self.redirect(self.request.get('redirect_link'))


# This non-constant name is okay; pylint: disable=C0103
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/vote_board/(.*)', VoteBoardPage),
    ('/vote/(.*)', VotePage),
    ('/viewed/(.*)', ViewedPage),
    ('/admin/load', DataLoadPage),
], debug=True)
