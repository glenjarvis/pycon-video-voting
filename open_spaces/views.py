"""Views to support PyCon Open Spaces Board"""

from django.shortcuts import render, redirect, reverse
from django.forms import ModelForm

from .models import OpenSpace


class OpenSpaceForm(ModelForm):
    class Meta:
        model = OpenSpace
        fields = ['topic', 'host', 'meeting_type', 'invitation']

def open_spaces_board(request):
    open_spaces = list(OpenSpace.objects.all())

    return render(request,
                  'open_spaces/board.html',
                  {'open_spaces': open_spaces})


def space(request, space_id):
    space = OpenSpace.objects.get(id=space_id)

    return render(request,
                  'open_spaces/space.html',
                  {'space': space})


def new_space(request):
    if request.method == "POST":
        form = OpenSpaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('open-spaces-board'))
        else:
            return render(request,
                         'open_spaces/new_space.html',
                         {'form': form})

    else:
        form = OpenSpaceForm()
        return render(request,
                     'open_spaces/new_space.html',
                     {'form': form})

