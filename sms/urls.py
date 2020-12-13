from django.urls import path
from . import views
from .models import Competition, Participant, User
from .forms import CompetitionForm, ParticipantForm, RefereeForm

urlpatterns = [
    path('', views.login, name='sms-login'),
    path('home/', views.home, name='sms-home'),

    # forms
    path('competition_form/', views.generic_form, {'form_object': CompetitionForm}, name='sms-TEST-FORM'),
    path('participant_form/', views.generic_form, {'form_object': ParticipantForm}, name='sms-TEST-FORM'),
    path('referee_form/', views.generic_form, {'form_object': RefereeForm}, name='sms-TEST-FORM'),
    path('TEST_FORM_SAVED/', views.saved_test_form, name='sms-TEST-FORM-SAVED'),

    # lists
    path('competition_list/', views.GenericList.as_view(model=Competition), name='sms-COMPETITION-LIST'),
    path('referee_list/', views.GenericList.as_view(model=User), name='sms-REFEREE-LIST'),
    path('participant_list/', views.GenericList.as_view(model=Participant), name='sms-PARTICIPANT-LIST'),

    # results
    path('bracket/', views.bracket, name='sms-bracket')
]
