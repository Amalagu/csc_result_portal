from accounts.models import Advisor, Student  
from portal.models import Semester, Session

def user_context(request):
    current_class_set = None
    portal_user = None

    if request.user.is_authenticated:
        try:
            student = Student.objects.get(student=request.user)
            current_class_set = student.student_class
            portal_user = student
        except Student.DoesNotExist:
            try:
                advisor = Advisor.objects.get(advisor=request.user)
                current_class_set = advisor.advisor_class
                portal_user = advisor
            except Advisor.DoesNotExist:
                current_class_set = None

        #current_semester = Semester.objects.get(iscurrentsemester=True)
        #current_session = Session.objects.get(iscurrentsession=True)

    return {'current_class_set': current_class_set,
            'portal_user' : portal_user,
            #'current_semester': current_semester,
            #'current_session' : current_session
            }

