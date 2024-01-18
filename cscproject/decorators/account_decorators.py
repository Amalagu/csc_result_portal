from django.shortcuts import render
from accounts.models import Advisor, Student

def advisor_required(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            advisor = Advisor.objects.get(advisor=request.user)
        except Advisor.DoesNotExist:
            return render(request, 'unauthorized.html')
        return view_func(request, *args, **kwargs)
    return wrapper


def student_required(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            student = Student.objects.get(student=request.user)
        except Student.DoesNotExist:
            return render(request, 'unauthorized.html')
        return view_func(request, *args, **kwargs)
    return wrapper
