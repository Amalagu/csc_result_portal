from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from portal.models import StudentClass #, DepartmentalDues
#from result.models import Result


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
    address = models.CharField(max_length=50, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/%y/%m/%d/', default='default.png', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.last_name + " " +  self.first_name 
        return full_name

    def get_picture(self):
        try:
            return self.picture.url
        except:
            no_picture = settings.MEDIA_URL + 'default.png'
            return no_picture
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.picture.path)
        except:
            pass
    
    def delete(self, *args, **kwargs):
        if self.picture.url != settings.MEDIA_URL + 'default.png':
            self.picture.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return '{} ({})'.format(self.get_full_name, self.email)




class Student(models.Model):
    level_list = (
        ('100 LEVEL', '100 LEVEL'),
        ('200 LEVEL', '200 LEVEL' ),
        ('300 LEVEL', '300 LEVEL'),
        ('400 LEVEL', '400 LEVEL'),
        ('500 LEVEL', '500 LEVEL')
    )
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, null=True, blank=True, on_delete=models.SET_NULL, related_name='students')
    registeration_number = models.CharField(max_length=11, null=False, blank=False, primary_key=True, unique=True)
    level = models.CharField(max_length=25, choices=level_list, null=True)

    cgpa = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)

    def update_cgpa(self, cgpa):
        self.cgpa = cgpa
        self.save()
        """ from result.models import Result
        results = Result.objects.filter(student=self)
        if results.exists():
            cumm_points = sum(result.tgp if result.tgp is not None else 0 for result in results)
            cumm_units = sum(result.tnu if result.tnu is not None else 0 for result in results)
            new_cgpa = cumm_points / cumm_units if cumm_units != 0 else 0.0
        else:
            new_cgpa = None

        # Check if the cgpa has changed before saving
        if self.cgpa != new_cgpa:
            self.cgpa = new_cgpa
            self.save()

    def save(self, *args, **kwargs):
        self.update_cgpa()
        super().save(*args, **kwargs) """
        


    def __str__(self):
        return self.student.get_full_name
    


class Advisor(models.Model):
    advisor = models.OneToOneField(User, on_delete=models.CASCADE)
    advisor_class = models.ForeignKey(StudentClass, null= True, on_delete=models.SET_NULL)
    staffid = models.CharField(max_length=12, unique=True, blank=False, null=False)
    designation = models.CharField(max_length=10, choices=designation_list)

    def __str__(self):
        return self.advisor.get_full_name
