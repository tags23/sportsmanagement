from django import forms
from .models import Competition, Participant, User # User = referee


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


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            # 'gender': forms.Select(attrs={'class': 'form-control'}, choices=('F', 'M')),  # only 2 genders
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RefereeForm(forms.ModelForm):
    class Meta:
        model = User  # bleh, does not match the class name...
        fields = ['name', 'surname', 'phone', 'qualification',
                  'username', 'email', 'password']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
