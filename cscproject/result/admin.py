from django.contrib import admin
from .models import RegisteredCourse, Result, UploadedFile
# Register your models here.

admin.site.register(RegisteredCourse)
admin.site.register(Result)
admin.site.register(UploadedFile)
