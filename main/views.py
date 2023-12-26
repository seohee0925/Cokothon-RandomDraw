from django.shortcuts import render, get_object_or_404

from accounts.models import Accounts
from .models import Capsule, picked_capsule
from .forms import CapsuleCreateForm

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

def write_capsule(request):
    # user_email = Accounts.objects.get(email=email)
    user_email = request.session['email']
    user = Accounts.objects.get(email=user_email) # 해당 정보를 가져옴

    if request.method == 'POST':
        form = CapsuleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # form.instance.email = user_email
            form.save()
            # return JsonResponse()
            return render(request, 'show_capsule.html')
    else:
        form = CapsuleCreateForm()
    return render(request, 'write_capsule.html', {'form': form})

def show_capsule(request, id): # 사용자 제외 랜덤
    if request.method == 'GET':
        capsule = get_object_or_404(Capsule, id=id)

        # return render(request, 'show_capsule.html', {'capsule' : capsule})
        return JsonResponse({'id' : capsule.id, 'content':capsule.content}, json_dumps_params={'ensure_ascii':False}, content_type = 'application/json; charest=utf-8')
