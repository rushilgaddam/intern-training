from django.urls import path, include
from django.http import HttpResponse
from django.contrib import admin
from detection.views import FrontendAppView

from django.conf import settings
from django.conf.urls.static import static
import os

def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('detection.urls')),
    path('', FrontendAppView.as_view(), name='frontend')
]

urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'detection/static'))
