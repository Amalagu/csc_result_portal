from django.urls import path
from .views import (
    student_lib_home, 
    student_lib_book_details,
    student_lib_book_read,
    student_lib_search_result,
    staff_lib_book_detail,
    staff_lib_book_read,
    staff_lib_home,
    staff_lib_upload_book,
    books_api,
    star_book,
) 


urlpatterns = [
    path('', student_lib_home, name='student_lib_home' ),
    path('<int:pk>/', student_lib_book_details, name='student_lib_book_detials'),
    path('<int:pk>/read', student_lib_book_read, name='student_lib_book_read'),
    path('search-result', student_lib_search_result, name='student_lib_search_result'),
    path('staff', staff_lib_home, name='staff_lib_home'),
    path('staff/<int:pk>/', staff_lib_book_detail, name='staff_lib_book_detail'),
    path('staff/<int:pk>/read', staff_lib_book_read, name='staff_lib_book_read'),
    path('staff/upload', staff_lib_upload_book, name='staff_lib_upload_book'),
    path('starbook/<int:pk>/', star_book, name='star_book' ),
    #API
    path('api/', books_api, name='bookapi'),

]