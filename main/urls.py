from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('filter/', views.write_capsule, name='write_capsule'),
    path('filter/<int:id>/', views.show_capsule, name='show_capsule'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)