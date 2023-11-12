from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "other_names", "last_name", "phone_number")

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "other_names", "last_name", "phone_number")