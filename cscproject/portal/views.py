from django.shortcuts import render
from accounts.models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_view(request):
    student = Student.objects.get(student=request.user)
    context = {'student': student}
    return render(request, 'portal/home.html', context)