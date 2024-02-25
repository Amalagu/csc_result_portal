from django.urls import path
from .views import add_course, course_registeration, view_course_registerations, course_registeration_borrow_course, view_course_registeration_details





urlpatterns = [
    path('add/', add_course, name='add_course'),
    path('register/', course_registeration, name='course_registeration' ),
    path('register-borrowed-course/', course_registeration_borrow_course, name='course_registeration_borrow_course' ),
    path('view/<str:session>/<str:semester>/', view_course_registeration_details, name='view_course_registeration_details'),
    path('view/', view_course_registerations, name='view_course_registerations')
]