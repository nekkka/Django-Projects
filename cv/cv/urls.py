
from django.contrib import admin
from django.urls import path

urlpatterns = [ 
    path('contact/', contact_view, name='contact'), 
] 
