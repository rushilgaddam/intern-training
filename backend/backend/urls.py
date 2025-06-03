from django.urls import path, include
from django.http import HttpResponse
from django.contrib import admin

def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('detection.urls')),
    path('', home),  
]
