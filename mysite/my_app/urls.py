
from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_syte , name= 'mys_site'),
 
]