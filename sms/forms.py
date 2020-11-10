from django import forms
from .models import Competition


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['address', 'date', 'time', 'sport', 'comp_format', 'comp_name', 'no_of_participants']
