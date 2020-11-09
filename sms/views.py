from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'sms/login.html', context={"title": "SMS: Login"})


def home(request):
    return render(request, 'sms/home.html', context={"title": "SMS: Home"})
