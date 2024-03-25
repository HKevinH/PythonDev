

from typing import Any
from django import forms
from .models import  Transaction, Client, Account, AccountCurrent, AccountSaving
import uuid
from django.db import transaction
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
    
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['balance', 'client']
    def generate_account_number(self):
        return str(uuid.uuid4().int)[:10]

    @transaction.atomic
    def save(self, commit=True, account_type=None, **kwargs):
        account = super().save(commit=False)
        account.number_account = self.generate_account_number()
        account_current = None
        account_saving = None
        client_id  = kwargs.get('client_id')
        if client_id is None:
            raise ValueError("client_id is required")
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            raise ValueError("Client with id {} does not exist".format(client_id))

        account.client = client
        
        if account.client: 
            print("Detalles de account.client:")
            for field in account.client._meta.fields:
                field_name = field.name
                field_value = getattr(account.client, field_name, 'No definido')
                print(f"{field_name}: {field_value}")
        else:
            print("account.client no está definido.")

        if commit:
            account.save()  
            
        if account_type == 'saving':
            interest_rate = kwargs.get('interest_rate', 0)
            account_saving = AccountSaving.objects.create(account_ptr_id=account.client_id, interest_rate=interest_rate)
            return account_saving
        elif account_type == 'current':
            limit = kwargs.get('limit', 0)
            account_current = AccountCurrent.objects.create(account_ptr_id=account.client_id, limit=limit)
            return account_current
        else:
            return account
    
    
# Natural Person Form
class AccountSavingForm(forms.ModelForm):
    class Meta:
        model = AccountSaving
        fields = ['interest_rate']
        

# Business Person Form

class AccountCurrentForm(forms.ModelForm):
    class Meta:
        model = AccountCurrent
        fields = ['limit']
        
    
        
    
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'value', 'type']



# Generated Reports
