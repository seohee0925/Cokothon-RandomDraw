from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import accountForm 
from .models import Accounts
# Create your views here.

@csrf_exempt
def register(request):
    print(request.body)
    requestdata = json.loads(request.body.decode('utf-8'))
    print(requestdata)

    emaildata = requestdata['email'] 
    namedata = requestdata['name']
    passworddata = requestdata['password']


    data = Accounts(email = emaildata, name = namedata, password = passworddata)
    data.save()
    # AccountForm = accountForm(request.POST)
    # cleaned_data = AccountForm.cleaned_data
    # form = json.dumps(cleaned_data)
    # print(form)

    # print(AccountForm.email)

    # AccountForm.fields['email'].initial = emaildata
    # AccountForm.fields['name'].initial = namedata
    # AccountForm.fields['password'].initial = passworddata

    # AccountForm.email = emaildata
    # print(AccountForm.email)
    # AccountForm.name = namedata
    # AccountForm.password = passworddata

    return JsonResponse({'result' : 'success'}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

@csrf_exempt
def login(request):
    requestdata = json.loads(request.body.decode('utf-8'))
    requestdata = json.loads(request.body)
    print(requestdata)

    emaildata = requestdata['email']
    passworddata =  requestdata['password']

    request.session['email'] = emaildata
    

    try:
        account = get_object_or_404(Accounts, email = emaildata, password = passworddata)
    except:
        return JsonResponse({'result' : "fail"}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')
    
    print(account.id)
    return JsonResponse({'result' : "success"}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

def duam(request):

    print(request.session['email'])
    return JsonResponse({'result' : "success"}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')



