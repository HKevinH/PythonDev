from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClientForm, AccountForm, AccountSavingForm, AccountCurrentForm
from .models import Client
from django.contrib.auth.hashers import check_password
from .helpers import get_common_context, saveClientLogin 
from django.contrib.auth.decorators import login_required

# Create your views here.
def IndexView(request):
    context = get_common_context(request)
    return render(request, 'index.html', context)

def RegisterView(request):
    context = get_common_context(request)
    return render(request, 'register.html', context)  

def LoginView(request):
    context = get_common_context(request)
    return render(request, 'login.html' , context)

def ProfileView(request):
    context = get_common_context(request)
    return render(request, 'dashboard.html', context)

# Functions to create a client
def CreateCLient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
        return render(request, 'register.html', {'form': form})
    
    else:
        form = ClientForm()
        return render(request, 'register.html', {'form': form})

# Login

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            client = Client.objects.get(email=email)
            if check_password(password, client.password):
                res = saveClientLogin(request, client)
                return res
            else:
                return HttpResponse('Password is incorrect')
        except Client.DoesNotExist:
            return HttpResponse('Client not found')
    else:
        return render(request, 'login.html')


# Logout
def Logout(request):
    response = render(request, 'index.html')
    response.set_cookie('logged_in', 'False')
    return response

# AddCAccount
def AddAccount(request):
    if request.method == 'POST':
        account_type = request.POST.get('account_type')
        interest_rate = request.POST.get('interest_rate', None)
        limit = request.POST.get('limit', None)
        form = AccountForm(request.POST)
        client_id = request.session.get('client_id')
        
        if form.is_valid():
            account = form.save(commit=False, account_type=account_type, client_id=client_id)
            client = Client.objects.get(id=client_id)
            account.client = client
        if account_type == 'saving' and interest_rate is not None:
            account.interest_rate = interest_rate
        elif account_type == 'current' and limit is not None:
            account.limit = limit
        else:
            print(form.errors)
            return render(request, "dashboard.html", {"form": form, "error": "Datos faltantes o inválidos."})
        
        account.save()
        return redirect('profile')
    
    else:
        print(form.errors)
        form = AccountForm()
        print('no hubo request')
    return render(request, "dashboard.html", {"form": form})
            