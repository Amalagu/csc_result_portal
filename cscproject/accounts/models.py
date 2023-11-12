from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from portal.models import StudentClass
# Create your models here.


designation_list = (
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Dr.', 'Dr.'),
    ('Prof.', 'Prof'),
    ('Miss', 'Miss'),
    ('Ms.', 'Ms.')
)


class CustomUserManager(BaseUserManager):
    """
    Custom User model manager where email is the unique identifier for
    authentication instead of usernames
    """
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if kwargs.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **kwargs)


class User(AbstractUser):
    username=None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    other_names = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager

    @property
    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name

    def __str__(self):
        return '{} ({})'.format(self.get_full_name, self.email)




class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, null=True, on_delete=models.SET_NULL)
    registeration_number = models.CharField(max_length=11, null=False, blank=False, primary_key=True, unique=True)
    


class Advisor(models.Model):
    advisor = models.OneToOneField(User, on_delete=models.CASCADE)
    advisor_class = models.ForeignKey(StudentClass, null= True, on_delete=models.SET_NULL)
    staffid = models.CharField(max_length=12, unique=True, blank=False, null=False)
    designation = models.CharField(max_length=10, choices=designation_list)
