from rest_framework.routers import DefaultRouter 

from .views import UserViewSet, ProjectViewSet, CategoryViewSet, PriorityViewSet, TaskViewSet 

 

router = DefaultRouter() 

router.register(r'users', UserViewSet) 

router.register(r'projects', ProjectViewSet) 

router.register(r'categories', CategoryViewSet) 

router.register(r'priorities', PriorityViewSet) 

router.register(r'tasks', TaskViewSet) 

 

urlpatterns = router.urls 

Include the core.urls in the main urls.py: 

from django.contrib import admin 

from django.urls import path, include 

 

urlpatterns = [ 

    path('admin/', admin.site.urls), 

    path('api/', include('core.urls')), 

] 