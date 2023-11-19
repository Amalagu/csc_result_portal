from django.urls import path
from .views import add_course, course_registeration





urlpatterns = [
    path('add/', add_course),
    path('register/', course_registeration )
]