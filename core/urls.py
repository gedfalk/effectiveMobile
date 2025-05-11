from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

from main.views import index

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)