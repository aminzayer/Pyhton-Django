from django.urls import path
from my_site import views

urlpatterns = [
    path('', views.my_index_site, name='my_index_site'),
]
