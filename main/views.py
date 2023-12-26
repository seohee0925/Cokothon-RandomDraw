from django.shortcuts import render, get_object_or_404
from .forms import CapsuleCreateForm
from .models import Capsule
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

def write_capsule(request):
    if request.method == 'POST':
        form = CapsuleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'show_capsule.html')
    else:
        form = CapsuleCreateForm()
    
    return render(request, 'write_capsule.html', {'form': form})

def show_capsule(request, id):
    if request.method == 'GET':
        capsule = get_object_or_404(Capsule, id=id)

        # return render(request, 'show_capsule.html', {'capsule' : capsule})
        return JsonResponse({'id' : capsule.id, 'content':capsule.content}, json_dumps_params={'ensure_ascii':False}, content_type = 'application/json; charest=utf-8')
