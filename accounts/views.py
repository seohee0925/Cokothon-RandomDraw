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
    AccountForm = accountForm(request.POST)
    AccountForm.save()
    return JsonResponse({'result' : 'success'}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

@csrf_exempt
def login(request):
    # # requestdata = json.loads(request.body.decode('utf-8'))
    # requestdata = json.loads(request.body)
    # print(requestdata)

    emaildata = request.POST.get('email')
    namedata =  request.POST.get('name')

    request.session['email'] = emaildata

    try:
        account = get_object_or_404(Accounts, email = emaildata, name = namedata)
    except:
        return JsonResponse({'result' : "fail"}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')
    
    print(account.id)
    return JsonResponse({'result' : "success"}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

def duam(request):

    print(request.session['email'])
    return JsonResponse({'result' : "success"}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')



