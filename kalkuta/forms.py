from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import datetime

class DodajPolog(forms.Form):
    polog_visina = forms.FloatField(label="POLOG VISINA FORM")


class DodajStrosek(forms.Form):
    strosek_visina = forms.FloatField(label="Strosek visina form")

class DodajCilj(forms.Form):
    ime_cilja = forms.CharField(label='Uporabnisko ime', max_length=30)
    visina_cilja = forms.FloatField(label="CILJ VISINA FORM")
    rok = forms.DateField(initial=datetime.date.today)

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Uporabnisko ime', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Geslo',
                          widget=forms.PasswordInput())
    password2 = forms.CharField(label='Geslo (ponovno)',
                        widget=forms.PasswordInput())



    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Gesli se ne ujemata.')


    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Uporabnisko ime lahko vsebuje le alfanumercine znake in podpicje.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Uporabnisko ime je ze zasedeno.')
