from django.shortcuts import render, redirect, get_object_or_404
from decorators.account_decorators import advisor_required, student_required
from accounts.models import Student
from result.models import RegisteredCourse
from portal.models import Semester, Session
from .forms import CourseModelForm
from django.http import HttpResponse

# Create your views here.

""" def course_registeration_details(request, pk=0):
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
    return render(request, 'course/course-registration-details.html') """


@student_required
def view_course_registeration_details(request, session, semester):
    all_current_semester_registered_courses = RegisteredCourse.objects.filter(session=session, semester=semester, student=request.user.student)
    context={
        'all_current_semester_registered_courses' : all_current_semester_registered_courses,
    }
    return render(request, 'course/course-registration-details.html', context)


@student_required
def view_course_registerations(request):
    registered_semesters = RegisteredCourse.objects.values('session', 'semester', 'student__level').distinct()
    print(registered_semesters)
    context = {
        'registered_semesters': registered_semesters,
        }
    return render(request, 'course/courses.html', context)


@student_required
def course_registeration(request):
    current_semester = Semester.objects.get(iscurrentsemester=True)
    if request.method == 'POST':
        pass
    else:
        pass
        #student = get_object_or_404(Student, student=request.user)
        #student = Student.objects.get(student=request.user).get_related('level')
        #taken_courses = RegisteredCourse.objects.filter(student__student=request.user, level=student.level, semester=current_semester)
        return render(request, "course/course-registration.html")


@student_required
def course_registeration_borrow_course(request):
    return render(request, "course/course-registration-borrow-courses.html")

""" @student_required
def course_registeration_details(request):
    return render(request, 'course/course-registration-details.html') """


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