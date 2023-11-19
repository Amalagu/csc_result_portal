from django.urls import path
from .views import parsetoresultmodel, upload_file


urlpatterns = [
    path('', parsetoresultmodel),
    path('upload/', upload_file),

]