
from django.contrib import admin
from django.urls import path
from cv.views import contact_view

urlpatterns = [ 
    path('contact/', contact_view, name='contact'), 
] 
