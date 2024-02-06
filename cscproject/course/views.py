from django.shortcuts import render, redirect, get_object_or_404
from decorators.account_decorators import advisor_required, student_required
from accounts.models import Student
from result.models import RegisteredCourse
from portal.models import Semester, Session
from course.models import Course
from .forms import CourseModelForm
from django.http import HttpResponse
from django.db.models import Q

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
    total_registered_units = sum( registerdcourse.course.unit for registerdcourse in all_current_semester_registered_courses)
    context={
        'all_current_semester_registered_courses' : all_current_semester_registered_courses,
        'total_registered_units' : total_registered_units,
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
    current_session = Session.objects.get(iscurrentsession=True)
    student= Student.objects.get(student=request.user)
    registered_courses_instances = RegisteredCourse.objects.filter(student=student, session=current_session, semester=current_semester)
    registered_courses = registered_courses_instances.values_list('course__code', flat=True)
    """SINCE THE REGISTERED COURSES MIGHT CONTAIN BORROWED COURSES FROM OTHER LEVELS THAT IS NOT
    CAPTURED IN current semester courses WE NEED TO MERGE BOTH QUERYSET. BUT WE NEED BOTH
    QUERYSET TO CONTAIN SAME TYPE OF INSTANCES - WHICH IS 'COURSE' """
    #registered_course_instances = registered_courses.values_list('course', flat=True) #GET THE QUERYSET OF COURSES
    print('THIS IS REGISTERED COURSE', registered_courses)
    merged_courses = Course.objects.filter(semester=current_semester, level=request.user.student.level) | Course.objects.filter(registeredcourse__in=registered_courses_instances) #MERGE BOTH OF THEM
    merged_courses = merged_courses.distinct()
    registered_coursecodes_list = list(registered_courses)
    context = {
        'registered_coursecodes_list':registered_coursecodes_list,
        'merged_courses':merged_courses,
    }
    if request.method == 'POST':
        selected_courses = request.POST.getlist('selected_courses')
        deregistered_courses = set(registered_coursecodes_list)- set(selected_courses)
        newly_selected_courses = list(set(selected_courses) - set(registered_coursecodes_list))
        new_registerations = []
        for coursecode in newly_selected_courses:
            courseobject = Course.objects.filter(code=coursecode).first()
            new_course, created = RegisteredCourse.objects.get_or_create(
                student=student,
                course=courseobject, 
                semester=current_semester, 
                session=current_session
                )
            if created:
                new_registerations.append(new_course)
        #RegisteredCourse.objects.bulk_create(new_registerations)
        RegisteredCourse.objects.filter(
            student=student, 
            session=current_session, 
            semester=current_semester, 
            course__code__in=deregistered_courses
            ).delete()
        return redirect('course_registeration')
    return render(request, "course/course-registration.html", context )


@student_required
def course_registeration_borrow_course(request):
    current_semester = Semester.objects.get(iscurrentsemester=True)
    current_session = Session.objects.get(iscurrentsession=True)
    student= Student.objects.get(student=request.user)
    registered_courses_instances = RegisteredCourse.objects.filter(student=student, session=current_session, semester=current_semester)
    all_courses = Course.objects.all()
    unregistered_courses = all_courses.exclude(registeredcourse__in=registered_courses_instances).order_by('level')
    if request.method == 'POST':
        selected_courses = request.POST.getlist('selected_courses')
        new_registerations = []
        for coursecode in selected_courses:
            courseobject = Course.objects.filter(code=coursecode).first()
            new_course, created = RegisteredCourse.objects.get_or_create(
                student=student,
                course=courseobject, 
                semester=current_semester, 
                session=current_session
                )
        return redirect('course_registeration')
    context={
        'unregistered_courses': unregistered_courses,
    }
    return render(request, "course/course-registration-borrow-courses.html", context)





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