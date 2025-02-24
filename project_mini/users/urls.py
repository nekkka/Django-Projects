from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

"""
urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    #path('users/', UserListView.as_view(), name='users'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', user_list_view, name='user_list'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]"""

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='users'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]