from django.shortcuts import render, redirect

from .forms import UserCreationForm, StudentForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from decorators.account_decorators import student_required, advisor_required
from .forms import LoginForm, UserModelForm
from .models import Student, Advisor
# Create your views here.


"""from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student, Advisor

@login_required
def dashboard_view(request):
    user = request.user

    # Check if the user is a student
    try:
        student = Student.objects.get(student=user)
        return render(request, 'student_dashboard.html', {'student': student})
    except Student.DoesNotExist:
        pass

    # Check if the user is an advisor
    try:
        advisor = Advisor.objects.get(advisor=user)
        return render(request, 'advisor_dashboard.html', {'advisor': advisor})
    except Advisor.DoesNotExist:
        pass

    # If the user is neither a student nor an advisor, you can handle it accordingly
    return render(request, 'unauthorized.html')
"""


@login_required
def testview(request):
    return render(request, "course-registration.html")


@login_required
@student_required
def view_student_profile(request):
    student = Student.objects.get(student=request.user);
    if request.method == 'POST':
        form = UserModelForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserModelForm(instance=request.user)
    context = {
        "student":student,
        'form': form
    }
    return render(request, 'accounts/profile.html', context)



@login_required
@advisor_required
def view_advisor_profile(request):
    advisor = Advisor.objects.get(advisor=request.user)

    if request.method == 'POST':
        form = UserModelForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_advisor_profile')  # Redirect to the advisor profile page or wherever you want
    else:
        form = UserModelForm(instance=request.user)

    context = {
        "advisor": advisor,
        'form': form
    }
    return render(request, 'accounts/advisor-profile.html', context)



""" @advisor_required
def view_advisor_profile(request):
    advisor = Advisor.objects.get(advisor=request.user);
    form = UserModelForm(instance=advisor)
    
    context = {
        "advisor":advisor,
        'form': form
    }
    return render(request, 'accounts/advisor-profile.html', context) """



def register_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved Succesfully")
        print(form)
        return HttpResponse("Error")
    context = {'form': form}
    return render(request, 'accounts/login_signup_form.html', context)


def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if hasattr(user, 'student'):
                    return redirect('home')
                # Check if the user is an Advisor
                elif hasattr(user, 'advisor'):
                    return redirect('advisor_home')
            else:
                messages.error(request, 'Invalid username or password')
                print('Username not found')
        else:
            print('Username does not exist')
    else:
        login_form = LoginForm()
    return render(request, 'accounts/newlogin.html', {'form': login_form} )


def logout_view(request):
    logout(request)
    print("USER IS LOGGED OUT")
    return redirect('home')