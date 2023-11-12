from django.db import models
from accounts.models import Student
from portal.models import Session, Semester, StudentClass
from course.models import Course
# Create your models here.


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

level_list = (
        ('100 LEVEL', '100 LEVEL'),
        ('200 LEVEL', '200 LEVEL' ),
        ('300 LEVEL', '300 LEVEL'),
        ('400 LEVEL', '400 LEVEL'),
        ('500 LEVEL', '500 LEVEL')
    )

class RegisteredCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    testscore = models.IntegerField()
    labscore = models.IntegerField()
    examscore = models.IntegerField()
    totalscore = models.IntegerField()
    grade = models.CharField(max_length=1, choices=grade_list)
    remark = models.CharField(max_length=4, default='PASS', choices=remark_list)




class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(RegisteredCourse, on_delete=models.CASCADE)
    gpa = models.FloatField(null=True)
    cgpa = models.FloatField(null=True)
    level = models.CharField(max_length=25, choices=level_list, null=True)

