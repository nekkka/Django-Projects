from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpattern = [
    path('', views.index, name="index")
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls'))
]


