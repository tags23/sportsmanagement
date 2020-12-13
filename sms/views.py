from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.core import serializers

from .forms import CompetitionForm
from .models import Competition, Participant


def login(request):
    return render(request, 'sms/login.html', context={"title": "SMS: Login"})


def home(request):
    return render(request, 'sms/home.html', context={"title": "SMS: Home"})


def generic_form(request, form_object):
    """
    A default form view that should get the model from context, to automatically
    generate the front-end input fields.
    """

    if request.method == 'POST':
        form = form_object(request.POST)

        if form.is_valid():
            new_form_item = form.save()
            return HttpResponseRedirect('/TEST_FORM_SAVED/')
        else:
            print("Error with form: " + str(form.errors))
    else:
        # request context is important here
        # TODO: we have to know if it's in edit mode or new item mode
        form = form_object()

    return render(request, 'sms/form.html', context={'form': form, 'submit_text': "Pievienot"})


def saved_test_form(request):
    return render(request, 'sms/form_saved.html')


def bracket(request):
    participants = Participant.objects.all()
    part_serialized = serializers.serialize('json', participants)
    print(part_serialized)
    return render(request, 'sms/bracket.html', context={"title": "SMS: Bracket", "participants": part_serialized})


class GenericList(ListView):
    """
    A default view that displays any of the necessary
    lists we have in our system
    """
    # model = Competition  # Note: the template name 'competition_list.html' is inferred from the model
    # an object_list iterable is passed to the template


