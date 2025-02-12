from django.contrib import admin
from django.urls import path
from pdf import views
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accept, name="accept"),
    path('<int:id>/', views.resume, name="resume"),
    path('list/', views.list, name="list"),
    path('contact/', views.contact_view, name='contact'), 
    path('create-cv/', views.create_cv, name='create_cv'),
    path('share/email/<int:cv_id>/', views.share_cv_email, name='share_cv_email'),
    path('cv/list/', views.cv_list, name="cv_list"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
