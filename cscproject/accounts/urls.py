from django.urls import path, include
from .views import login_view, register_view, logout_view, view_profile

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', view_profile, name='view_profile')
]
