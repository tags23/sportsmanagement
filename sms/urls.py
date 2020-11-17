from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='sms-login'),
    path('home/', views.home, name='sms-home'),
    path('test_form/', views.generic_form, name='sms-TEST-FORM')
]
