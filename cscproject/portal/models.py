from django.db import models
#from accounts.models import Student, Advisor

# Create your models here.
level_list = (
        ('100 LEVEL', '100 LEVEL'),
        ('200 LEVEL', '200 LEVEL' ),
        ('300 LEVEL', '300 LEVEL'),
        ('400 LEVEL', '400 LEVEL'),
        ('500 LEVEL', '500 LEVEL')
    )


semester_list = (
    ('RAIN', 'RAIN'),
    ('HARMATTAN', 'HARMATTAN')
)




class StudentClass(models.Model):
    class_set = models.CharField(max_length=9, primary_key=True, unique=True)
    current_level = models.CharField(choices=level_list, max_length=10)
    enrollment_year = models.CharField(max_length=4)

    def __str__(self):
        return f'Class of {self.class_set}'


class Session(models.Model):
    name = models.CharField(max_length=9, primary_key=True, unique=True)
    iscurrentsession = models.BooleanField(default=False)
    start_date = models.DateField(unique=True)
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=20, choices=semester_list, unique=True, primary_key=True)
    iscurrentsemester = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class DepartmentalDues(models.Model):
    #student = models.ForeignKey(Student)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)