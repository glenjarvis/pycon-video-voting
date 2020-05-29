"""Views to support PyCon Video Voting"""

from django.shortcuts import render, redirect, reverse

from .models import Event, Talk



def voting_closed(request):
    """Close board for another year"""

    return render(request,
                  'vote/voting_closed.html')


def vote_board(request):
    """Display vote board for event given by event_id"""

    talks = list(Talk.objects.all().filter(viewed=False).order_by('-score'))

    return render(request,
                  'vote/vote_board.html',
                  {'talks': talks})

def vote(request, talk_id):
    """Increase score for talk with given talk_id"""

    talk = Talk.objects.get(id=talk_id)
    talk.score = talk.score + 1
    talk.save()

    return redirect(reverse('vote-board'))


def event_list(request):
    """Display list of events that have Voting Boards

    Note: This originally ported from Google App Engine when there was not a
          Django admin. There is There is currently only one event, thus this
          event_list is not curently being used.

    """

    return render(request,
                  'vote/index.html',
                  {'events': Event.objects.all()})
