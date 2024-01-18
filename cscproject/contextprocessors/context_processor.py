from accounts.models import Advisor, Student  

def user_context(request):
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

    return {'current_class_set': current_class_set,
            'portal_user' : portal_user
            }

