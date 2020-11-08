from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='sms-login'),
    path('home/', views.home, name='sms-home'),
]
