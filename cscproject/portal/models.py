from django.db import models

# Create your models here.
level_list = (
        ('100 LEVEL', '100 LEVEL'),
        ('200 LEVEL', '200 LEVEL' ),
        ('300 LEVEL', '300 LEVEL'),
        ('400 LEVEL', '400 LEVEL'),
        ('500 LEVEL', '500 LEVEL')
    )

grade_list=(
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F')
)

remark_list = (
    ('PASS', 'PASS'),
    ('FAIL', 'FAIL')
)

semester_list = (
    ('RAIN', 'RAIN'),
    ('HARMATTAN', 'HARMATTAN')
)

unit_list = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (6, 6)
)


designation_list = (
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Dr.', 'Dr.'),
    ('Prof.', 'Prof'),
    ('Miss', 'Miss'),
    ('Ms.', 'Ms.')
)

class StudentClass(models.Model):
    class_set = models.CharField(max_length=9, primary_key=True, unique=True)
    current_level = models.CharField(choices=level_list, max_length=10)
    enrollment_year = models.CharField(max_length=4)



class Student(models.Model):
    student_class = models.ForeignKey(StudentClass)
    registeration_number = models.CharField(max_length=11, null=False, blank=False, primary_key=True, unique=True)
    surname= models.CharField(max_length=40, blank=False, null=False)
    other_names = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=15)


class Advisor(models.Model):
    advisor_class = models.ForeignKey(StudentClass)
    staffid = models.CharField(max_length=12, unique=True, blank=False, null=False)
    designation = models.CharField(max_length=10, choices=designation_list)
    surname= models.CharField(max_length=40, blank=False, null=False)
    other_names = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=15)




class Session(models.Model):
    name = models.CharField(max_length=7, primary_key=True, unique=True)
    iscurrentsession = models.BooleanField(default=False)
    start_date = models.DateField(unique=True)
    end_date = models.DateField()

class Semester(models.Model):
    name = models.CharField(max_length=20, choices=semester_list, unique=True, primary_key=True)
    iscurrentsemester = models.BooleanField(default=False)


class Course(models.Model):
    code = models.CharField(max_length=7, unique=True, blank=False, null=False)
    title = models.CharField(max_length=140, blank=False, null=False)
    unit = models.IntegerField(choices=unit_list)
    semester = models.ForeignKey(Semester)
    iselective = models.BooleanField()


class RegisteredCourse(models.Model):
    student_id = models.ForeignKey(Student)
    course_id = models.ForeignKey(Course)
    student_class = models.ForeignKey(StudentClass)
    session = models.ForeignKey(Session)
    semester = models.ForeignKey(Semester)
    testscore = models.IntegerField()
    labscore = models.IntegerField()
    examscore = models.IntegerField()
    totalscore = models.IntegerField()
    grade = models.CharField(max_length=1, choices=grade_list)
    remark = models.CharField(max_length=4, default='PASS', choices=remark_list)



class Result(models.Model):
    student = models.ForeignKey(Student)
    session = models.ForeignKey(Session)
    semester = models.ForeignKey(Semester)
    course = models.ForeignKey(RegisteredCourse)
    gpa = models.FloatField(null=True)
    cgpa = models.FloatField(null=True)

