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

filetype_list = (
    ('Class list', 'Class list'),
    ('Result Sheet', 'Result Sheet')
)




class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    #course = models.ForeignKey(RegisteredCourse, on_delete=models.CASCADE)
    tgp = models.IntegerField(null=True, blank=True)
    tnu = models.IntegerField(null=True, blank=True)
    gpa = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    cummulative_tgp = models.IntegerField(null=True, blank=True)
    cummulative_tnu = models.IntegerField(null=True, blank=True)
    cgpa = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    level = models.CharField(max_length=25, choices=level_list, blank=True, null=True)
    student_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ('student', 'session', 'semester')

    @staticmethod
    def calculate_semester_gpa(student, session, semester):
        """static function to calculate the cgpa of a student for a particular
        semester in a session. You pass in the student's reg_number, a session object,
        and a semester object
        """
        grade_dict = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
        #student=Student.objects.get(registeration_number=student_id)
        result = Result.objects.filter(student=student, session=session, semester=semester).first()
        if result:
            courses = RegisteredCourse.objects.filter(result=result).exclude(grade__isnull= True)
            total_unit = sum(course.course.unit for course in courses if course.grade)
            total_points = sum(course.course.unit * grade_dict.get(course.grade, 0) for course in courses)
            gpa = total_points / total_unit if total_unit != 0 else 0.0
            result.tgp = total_points
            result.tnu = total_unit
            result.gpa = gpa
            return gpa, total_unit, total_points
        else:
            return 0.0, 0, 0
        


    @staticmethod
    def calculate_cgpa(student):
        """ static method to calculate a student's cgpa by querying the result table
        for other instances of their results for previous semesters.
        """
        results = Result.objects.filter(student=student).order_by('-id')
        if not results:
        # No results available, return a default CGPA (i.e 5.0)
            return 5.0, 0, 0
        most_recent_result = results.first()    #GET THE MOST RECENT RESULT
        cumm_points = sum(result.tgp if result.tgp is not None else 0 for result in results)
        cumm_units = sum(result.tnu if result.tnu is not None else 0 for result in results)
        cgpa = cumm_points / cumm_units if cumm_units != 0 else 0.0
        most_recent_result.cgpa = cgpa      #SAVE THE CURRENT CGPA VALUE TO THE MOST RECENT RESULT
        return cgpa,  cumm_units, cumm_points
    
    
    def save(self, *args, **kwargs):
        if self.pk:
            self.gpa, self.tnu, self.tgp = self.calculate_semester_gpa(student=self.student, semester=self.semester, session=self.session)
            super().save(*args, **kwargs)  # Save the instance first
            self.refresh_from_db()
            self.cgpa, self.cummulative_tnu, self.cummulative_tgp = self.calculate_cgpa(self.student)
            super().save(*args, **kwargs)  # Save the instance first
            self.student.update_cgpa()
        else:
            super().save(*args, **kwargs)
        
        

    def __str__(self):
        return f"{self.student.student.get_full_name} {self.semester.name} Results - {self.session.name} "



class RegisteredCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #student_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    testscore = models.IntegerField(null=True, blank=True)
    labscore = models.IntegerField(null=True, blank=True)
    examscore = models.IntegerField(null=True, blank=True)
    totalscore = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=1, choices=grade_list, null=True, blank=True)
    remark = models.CharField(max_length=4, default='PASS', choices=remark_list)
    result = models.ForeignKey(Result, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course', 'session', 'semester')

    def __str__(self):
        return self.student.student.get_full_name + ' - ' + self.course.code
    
    def save(self, *args, **kwargs):
        #Automatically create or update the related Result when saving ReigisteredCourse
        
        result, created = Result.objects.get_or_create(
            student = self.student,
            session = self.session,
            semester = self.semester,
            student_class = self.student.student_class,
            level=self.student.level
        )
        self.result = result
        if created:
            result.save()
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
            result.save()







class UploadedFile(models.Model):
    file_title = models.CharField(max_length=30, null=False, blank=False)
    type = models.CharField(max_length=30, choices=filetype_list, blank=False, null=False)
    excel_file = models.FileField(upload_to='uploads/')
    course_code = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, blank=True )
    session = models.ForeignKey(Session, null=True, blank=True, on_delete=models.SET_NULL)
    semester = models.ForeignKey(Semester, null=True, blank=True, on_delete=models.SET_NULL)
    class_set = models.ForeignKey(StudentClass, null=True, blank=True, on_delete=models.SET_NULL)
  



