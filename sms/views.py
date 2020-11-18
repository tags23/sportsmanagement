from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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

        if form.is_valid():
            new_form_item = form.save()
            return HttpResponseRedirect('/TEST_FORM_SAVED/')
    else:
        form = CompetitionForm()

    return render(request, 'sms/form.html', context={'form': form, 'submit_text': "Pievienot"})


def saved_test_form(request):
    return render(request, 'sms/form_saved.html')
