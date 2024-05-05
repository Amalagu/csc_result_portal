from django.db import models
from portal.models import Semester, Session
from accounts.models import Lecturer
# Create your models here.


unit_list = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (6, 6)
)


level_list = (
        ('100 LEVEL', '100 LEVEL'),
        ('200 LEVEL', '200 LEVEL' ),
        ('300 LEVEL', '300 LEVEL'),
        ('400 LEVEL', '400 LEVEL'),
        ('500 LEVEL', '500 LEVEL')
    )




class Course(models.Model):
    code = models.CharField(max_length=7, unique=False, blank=False, null=False)
    title = models.CharField(max_length=140, blank=False, null=False)
    unit = models.IntegerField(choices=unit_list)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    iselective = models.BooleanField()
    level = models.CharField(max_length=25, choices=level_list, null=True)

    class Meta:
        unique_together = ('code', 'title')

    def __str__(self):
        return self.code



class CourseAllocation(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name='allocated_lecturer')
    courses = models.ManyToManyField(Course, related_name='allocated_course')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.lecturer.staff.user.get_full_name



