from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import CapsuleViewSet

app_name = 'main'


urlpatterns = [
    path('write_capsule/', views.write_capsule, name='write_capsule'),
    path('show_capsule/', views.show_capsule, name='show_capsule'),
    path('show_all_picked_capsule/', views.show_all_picked_capsule, name='show_all_picked_capsule'),
    path('show_all_my_capsule/', views.show_all_my_capsule, name='show_all_my_capsule'),
    path('modal/', views.modal, name='modal')
]