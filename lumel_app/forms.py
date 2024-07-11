from crispy_forms.helper import FormHelper
from django import forms
from datetime import time


class CustomTimeInput(forms.TimeInput):
    def format_value(self, value):
        if isinstance(value, time):
            return value.strftime('%H:%M')
        return value


class ContactForm(forms.Form):
    EXPERTISES = [
        ('', 'Expertises'),
        ('Droit Immobilier', 'Droit Immobilier'),
        ('Droit Social', 'Droit Social'),
        ('Réparation du dommage corporel', 'Réparation du dommage corporel'),
        ('Droit Patrimonial', 'Droit Patrimonial'),
        ('Droit Commercial', 'Droit Commercial'),
        ('Autre', 'Autre'),
    ]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    telephone = forms.CharField(required=False, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Téléphone'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    heure = forms.TimeField(label='Heure', widget=CustomTimeInput(), initial=time(10, 30))
    expertise = forms.ChoiceField(choices=EXPERTISES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': 4, 'cols': 40}))



