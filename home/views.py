from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClientForm
from .models import Client
from django.contrib.auth.hashers import check_password

# Create your views here.
def IndexView(request):
    return render(request, 'index.html')

def RegisterView(request):
    return render(request, 'register.html')  

def LoginView(request):
    return render(request, 'login.html')

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


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            client = Client.objects.get(email=email)
            
            if check_password(password, client.password):
                return render(request, 'dashboard.html', {'client': client})
            else:
                return HttpResponse('Password is incorrect')
        except Client.DoesNotExist:
            return HttpResponse('Client not found')
    else:
        return render(request, 'login.html')
