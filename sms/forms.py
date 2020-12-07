from django import forms
from .models import Competition


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = '__all__'

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'}),
            'sport': forms.TextInput(attrs={'class': 'form-control'}),
            'comp_format': forms.TextInput(attrs={'class': 'form-control'}),
            'comp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'no_of_participants': forms.NumberInput(attrs={'class': 'form-control'}),
            'comp_status': forms.TextInput(attrs={'class': 'form-control'}),
        }
