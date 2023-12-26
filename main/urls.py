from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('filter/', views.write_capsule, name='write_capsule'),
    path('filter/<int:id>/', views.show_capsule, name='show_capsule'),
    path('show_all_picked_capsule/', views.show_all_picked_capsule, name='show_all_picked_capsule'),
    path('show_all_my_capsule/', views.show_all_my_capsule, name='show_all_my_capsule'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)