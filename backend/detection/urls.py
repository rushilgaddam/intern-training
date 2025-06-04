from django.urls import path, re_path
from . import views
from detection.views import FrontendAppView


urlpatterns = [
    path('log/', views.log_detection, name = "log_detection"),
]