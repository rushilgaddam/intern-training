from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_detection, name = "log_detection"),
]