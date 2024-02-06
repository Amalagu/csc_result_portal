from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserChangeForm, UserCreationForm
from .models import User, Student, Advisor
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


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Advisor)