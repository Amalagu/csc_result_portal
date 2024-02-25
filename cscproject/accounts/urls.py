from django.urls import path, include
from .views import login_view, register_view, logout_view, view_student_profile, testview, view_advisor_profile

urlpatterns = [
    path('test/', testview),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', view_student_profile, name='view_profile'),
    path('advisor/profile/', view_advisor_profile, name='view_advisor_profile')

]
