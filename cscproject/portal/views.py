from django.shortcuts import render
from accounts.models import Student
from portal.models import Semester, Session
from result.models import RegisteredCourse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_view(request):
    student = Student.objects.get(student=request.user);
    current_semester = Semester.objects.get(iscurrentsemester=True);
    current_session = Session.objects.get(iscurrentsession = True);
    current_registered_semester_courses = RegisteredCourse.objects.filter(student=student, semester=current_semester, session=current_session)
    context = {
        'student': student,
        'current_session' : current_session,
        'current_semester': current_semester,
        'current_registered_semester_courses' : current_registered_semester_courses
        }
    return render(request, 'portal/home.html', context)