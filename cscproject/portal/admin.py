from django.contrib import admin
from .models import Semester, Session, StudentClass, DepartmentalDues
# Register your models here.

admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(StudentClass)
admin.site.register(DepartmentalDues)
