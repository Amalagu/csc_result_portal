from django.shortcuts import render
from accounts.models import Student, Advisor
from portal.models import Semester, Session
from result.models import RegisteredCourse, Result, UploadedFile
from course.models import Course
from django.contrib.auth.decorators import login_required
from decorators.account_decorators import advisor_required, student_required
# Create your views here.


@login_required
@advisor_required
def view_class_list(request, pk=0):
    advisor = Advisor.objects.get(advisor=request.user)
    current_class_set = advisor.advisor_class
    all_students_info = Student.objects.filter(student_class=current_class_set).order_by('student__last_name').values('student__last_name', 'registeration_number', 'student__first_name')
    #all_students_info = all_students_info[:10]
    context = {
        'all_students_info' : all_students_info
    }
    print(all_students_info)

    return render(request, "portal/advisor-class-list.html", context)

@login_required
@advisor_required
def advisor_home_view(request):
    advisor = Advisor.objects.get(advisor=request.user)
    current_semester = Semester.objects.get(iscurrentsemester=True)
    current_session = Session.objects.get(iscurrentsession=True)
    current_class_set = advisor.advisor_class
    current_class_level = advisor.advisor_class.current_level
    number_of_students_in_class = advisor.advisor_class.students.count()
    number_of_semester_courses = Course.objects.filter(level=current_class_level, semester=current_semester).count()
    top_students = Student.objects.filter(student_class=current_class_set).exclude(cgpa=None).order_by('-cgpa')[:5]
    #top_students = Student.objects.filter(student_class=current_class_set, cgpa__isnull=False).order_by('-cgpa')[:5]
    results_uploaded = UploadedFile.objects.filter(session=current_session, semester=current_semester, class_set=current_class_set)

    print(top_students)
    context = {
        "advisor" : advisor,
        "current_session" : current_session,
        "current_semester" : current_semester,
        "advisor_fullname" : advisor.advisor.get_full_name,
        #"current_class_set" : current_class_set,
        "current_class_level" : current_class_level,
        "results_uploaded" : results_uploaded,
        "top_students" : top_students,
       "number_of_students_in_class" : number_of_students_in_class,
       "number_of_semester_courses" : number_of_semester_courses
    }
    return render(request, "portal/advisor-home.html", context)



@login_required
@student_required
def home_view(request):
    user = request.user
    student = Student.objects.get(student=request.user);
    current_semester = Semester.objects.get(iscurrentsemester=True);
    current_session = Session.objects.get(iscurrentsession = True);
    total_registered_semester_courses = RegisteredCourse.objects.filter(student=student)
    current_registered_semester_courses = total_registered_semester_courses.filter(semester=current_semester, session=current_session)
    cgpa = student.cgpa
    """ most_recent_cgpa = Result.objects.filter(student__registeration_number=student.registeration_number).order_by('-id').first()
    if most_recent_cgpa:
        most_recent_cgpa = most_recent_cgpa.cgpa
    else:
        most_recent_cgpa = 0.0 """
    context = {

        'student': student,
        'cgpa': cgpa,
        'current_session' : current_session,
        'current_semester': current_semester,
        'total_registered_semester_courses': total_registered_semester_courses,
        'current_registered_semester_courses' : current_registered_semester_courses
        }
    return render(request, 'portal/student-home.html', context)



