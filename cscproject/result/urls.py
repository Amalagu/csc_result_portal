from django.urls import path
from .views import (
    parsetoresultmodel, 
    upload_file, 
    student_view_result, 
    advisor_view_result, 
    view_all_courses_semester_result, 
    view_cgpa_summary,
    view_single_course_result,
    view_generated_transcript,
    view_generated_transcript_list
    )
from .api.views import ResultDataAPIView

urlpatterns = [
    path('view/', student_view_result, name="student_view_result"),
    path('advisor/view/', advisor_view_result, name="advisor_view_result"),
    #path('advisor/semester', view_all_courses_semester_result, name="all_semester_result"),
    path('advisor/semester', view_all_courses_semester_result, name="all_semester_result"),
    path('advisor/single', view_single_course_result, name="single_course_result"),
    path('advisor/summary', view_cgpa_summary, name='cgpa_summary'),
    path('advisor/transcript/<str:pk>/', view_generated_transcript, name="transcript"),
    path('advisor/transcript/', view_generated_transcript_list, name="list_trancript"),
    path('advisor/api', ResultDataAPIView.as_view()),

    path('', parsetoresultmodel),
    path('upload/', upload_file, name='uploadresult'),

]