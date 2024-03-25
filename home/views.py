from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClientForm
from .models import Client
from django.contrib.auth.hashers import check_password
from .helpers import get_common_context 
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
                response = render(request, 'dashboard.html', {'client': client})
                response.set_cookie('logged_in', 'True')
                return response
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

