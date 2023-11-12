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

class Course(models.Model):
    code = models.CharField(max_length=7, unique=True, blank=False, null=False)
    title = models.CharField(max_length=140, blank=False, null=False)
    unit = models.IntegerField(choices=unit_list)
    semester = models.ForeignKey(Semester)
    iselective = models.BooleanField()
