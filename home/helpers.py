from django.shortcuts import render, redirect
from django.http import HttpResponse


def get_common_context(request):
    logged_in = request.COOKIES.get('logged_in', 'False') == 'True'
    client_id = request.session.get('client_id')
    return {'logged_in': logged_in , 'client_id' : client_id }


def saveClientLogin(request : HttpResponse, client, account  ):
    response = render(request, 'dashboard.html', {'client': client, 'account': account})
    request.session['client_id'] = client.id
    request.session['client_name'] = client.name
    response.set_cookie('logged_in', 'True')
    return response
     
