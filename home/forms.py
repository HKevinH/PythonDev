

from typing import Any
from django import forms
from .models import Client, Account
from django.contrib.auth.hashers import make_password

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'password']
        
    
    def save(self, commit=True):
        # hashear la contraseña antes de guardarla
        user = super(ClientForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    