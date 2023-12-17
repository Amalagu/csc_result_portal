from django.urls import path
from .views import add_course, course_registeration, view_courses





urlpatterns = [
    path('add/', add_course, name='add_course'),
    path('register/', course_registeration, name='course_registeration' ),
    path('view/', view_courses, name='view_courses')
]