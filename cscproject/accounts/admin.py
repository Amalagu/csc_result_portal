from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserChangeForm, UserCreationForm
from .models import User, Student, Advisor, DepartmentStaff, Lecturer, DepartmentHead
# Register your models here.



class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("last_name",  "first_name", "email")
    list_filter = ("last_name",  "first_name", "email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields" : ("email", "password")}),
        (_('Personal info'), {"fields" : ("first_name", "last_name", "other_names", "phone_number")}),
        ("Permissions", {"fields" : ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes" : ("wide",),
            "fields" : (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "other_names",
                "first_name", "last_name"
            )
        }

        ),
    )
    search_fields = ("email",)
    ordering = ("email",)



class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'registeration_number',)  # Add other fields you want to display
    ordering = ['student__last_name']
    
    def get_full_name(self, obj):
        return f"{obj.student.last_name}, {obj.student.first_name}"  # Adjust as needed

    get_full_name.short_description = 'Full Name'  # Custom column header





admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Advisor)
admin.site.register(DepartmentStaff)
admin.site.register(DepartmentHead)
admin.site.register(Lecturer)