from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Student
from result.models import RegisteredCourse
from portal.models import Semester, Session
from .forms import CourseModelForm
from django.http import HttpResponse

# Create your views here.
def view_courses(request, pk=0):
    student = Student.objects.get(student=request.user);
    semester = Semester.objects.get(iscurrentsemester=True)
    session = Session.objects.get( iscurrentsession=True)
    current_registered_semester_courses = RegisteredCourse.objects.filter(student=student, session=session, semester=semester)
    if pk:
        highlighted_course = RegisteredCourse.objects.get(id=pk)
    else:
        highlighted_course = current_registered_semester_courses.first()
    context = {
        'student': student,
        'current_registered_semester_courses' : current_registered_semester_courses,
        'highlighted_course': highlighted_course
    }
    return render(request, 'course/courses.html', context)

def course_registeration(request):
    current_semester = Semester.objects.get(iscurrentsemester=True)
    if request.method == 'POST':
        pass
    else:
        #student = get_object_or_404(Student, student=request.user)
        student = Student.objects.get(student=request.user).get_related('level')
        taken_courses = RegisteredCourse.objects.filter(student__student=request.user, level=student.level, semester=current_semester)
        return HttpResponse('Course Registeration')


def add_course(request):
    form = CourseModelForm()
    if request.method == 'POST':
        print(request.POST)
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved Succesfully")
        return render(request, 'accounts/login_signup_form.html', {'form':form})
    return render(request, 'accounts/login_signup_form.html', {'form':form})