from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  
    path('api/products/', include('products.urls')),
    path('api/trading/', include('trading.urls')),
    path('api/sales/', include('sales.urls')),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)