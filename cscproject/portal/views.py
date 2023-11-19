from django.shortcuts import render
from accounts.models import Student
# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'portal/home.html', context)