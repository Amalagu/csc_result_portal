from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Student
from result.models import RegisteredCourse
from portal.models import Semester, Session
from .forms import CourseModelForm
from django.http import HttpResponse

# Create your views here.
def view_courses(request):
    return render(request, 'course/courses.html')

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