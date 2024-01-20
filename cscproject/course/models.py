from django.db import models
from portal.models import Semester, Session
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
    code = models.CharField(max_length=7, unique=True, blank=False, null=False)
    title = models.CharField(max_length=140, blank=False, null=False)
    unit = models.IntegerField(choices=unit_list)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    iselective = models.BooleanField()
    level = models.CharField(max_length=25, choices=level_list, null=True)

    def __str__(self):
        return self.code
