from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('filter/', views.write_capsule, name='write_capsule'),
    path('filter/<int:id>/', views.show_capsule, name='show_capsule'),
]