from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpattern = [
    path('', views.index, name="index")
]


urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
    path('update/<int:todo_id>', views.update, name="update"),
]

