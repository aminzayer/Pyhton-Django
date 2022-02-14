from django.urls import path
from . import views

# My app : domain.com/my_app/
urlpatterns = [
    path('', views.index, name='index')  # /my_app --> Project urls.py
]
