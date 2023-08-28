from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('contactus', views.contactus)
] 

# 127.0.0.1:8000