from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Accounts
from .models import Capsule, picked_capsule
# from .forms import CapsuleCreateForm
import json, random
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CapsuleSerializer
from rest_framework import viewsets
from rest_framework.views import APIView


class CapsuleViewSet(APIView):
    queryset = Capsule.objects.all() 
    serializer_class = CapsuleSerializer

    def get(self, request, **kwargs): 
        queryset = Capsule.objects.all()
        queryset_serializer = CapsuleSerializer(queryset, many=True)
        return Response(queryset_serializer.data)

    def post(self, request):
        user_email = "appleid5@naver.com"

        try:
            user = Accounts.objects.get(email=user_email)
        except Accounts.DoesNotExist:
            return Response("User not found", status=404)
        
        serializer = CapsuleSerializer(data=request.data, context={'user_email': user_email})

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)


    def perform_create(self, serializer):
        # Serializer의 save 메서드를 오버라이드하여 user_email을 저장
        serializer.save(email=self.request.data.get('email'))

    def list(self, request):
        serializer = CapsuleSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    # if request.method == 'POST':
    #     form = CapsuleCreateForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         new_capsule = form.save(commit=False)
    #         new_capsule.user = user
    #         new_capsule.email = user_email
    #         new_capsule.save()
    #         return JsonResponse({'success': True})
    # else:
    #     form = CapsuleCreateForm()
    # return render(request, 'write_capsule.html', {'form': form})

def show_capsule(request): 
    if request.method == 'GET':
        # user_email = request.session['email']
        # user = Accounts.objects.get(email=user_email)
        user_email = "app@naver.com"
        random_capsule = Capsule.objects.exclude(email=user_email)
        print(random_capsule)
        return JsonResponse({'id': random_capsule.id, 'content': random_capsule.content}, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')