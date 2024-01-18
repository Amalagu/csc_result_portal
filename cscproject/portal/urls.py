from django.urls import path
from .views import home_view, view_class_list, advisor_home_view

urlpatterns = [
    path('advisor/class', view_class_list, name="view_class_list"),
    path('advisor/', advisor_home_view, name='advisor_home'),
    path('', home_view, name='home'),
]