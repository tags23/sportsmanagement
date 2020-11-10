from django.shortcuts import render
from django.http import HttpResponse

from .forms import CompetitionForm


def login(request):
    return render(request, 'sms/login.html', context={"title": "SMS: Login"})


def home(request):
    return render(request, 'sms/home.html', context={"title": "SMS: Home"})


def generic_form(request):
    """
    A default form view that should get the model from context, to automatically
    generate the front-end input fields.
    """
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        # Add code to process the form
    else:
        form = CompetitionForm()
