from django.urls import path
from . import views


urlpatterns = [
    path('info', views.info), 
    path('profile/<username>', views.profile),   # 127.0.0.1:8000/acoount/amir
    path('userslist', views.userslist)
]