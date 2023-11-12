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

