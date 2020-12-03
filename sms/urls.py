from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='sms-login'),
    path('home/', views.home, name='sms-home'),
    path('test_form/', views.generic_form, name='sms-TEST-FORM'),
    path('TEST_FORM_SAVED/', views.saved_test_form, name='sms-TEST-FORM-SAVED'),
    path('test_list', views.GenericList.as_view(), name='sms-TEST-LIST')
]
