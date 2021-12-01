from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from image import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', views.photo_list, name='photo_list'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
