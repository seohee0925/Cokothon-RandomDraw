from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import accountForm 
# Create your views here.

@csrf_exempt
def register(request):
    # if request.method == 'POST':
    AccountForm = accountForm(request.POST)
        # if AccountForm.is_vaild():
    AccountForm.save()
    print("성공?")
    return JsonResponse({'result' : 'success'}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')


    # else:
    #     print("실패?")
    #     return JsonResponse({'result' : 'fail'}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')


def account(request):
    AccountForm = accountForm(request.POST)
    AccountForm.save()
    return render(request, 'account.html' ,{'form': AccountForm})