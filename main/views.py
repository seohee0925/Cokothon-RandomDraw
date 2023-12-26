from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Accounts
from .models import Capsule, picked_capsule
from .forms import CapsuleCreateForm

import datetime

import json, random
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

@login_required
def write_capsule(request):
    user_email = request.session['email']
    user = Accounts.objects.get(email=user_email)

    if request.method == 'POST':
        form = CapsuleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_capsule = form.save(commit=False)
            new_capsule.user = user
            new_capsule.email = user_email
            new_capsule.save()
            return JsonResponse({'success': True})
    else:
        form = CapsuleCreateForm()
    return render(request, 'write_capsule.html', {'form': form})

@login_required
def show_capsule(request, id): # 사용자 제외 랜덤
    if request.method == 'GET':
        user_email = request.session['email']
        user = Accounts.objects.get(email=user_email)

        capsules_exclude_user = Accounts.objects.exclude(user=user)
        random_capsule = random.choice(capsules_exclude_user)

        return JsonResponse({'id' : random_capsule.id, 'content':random_capsule.content}, json_dumps_params={'ensure_ascii':False}, content_type = 'application/json; charest=utf-8')

