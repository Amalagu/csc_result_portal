from django.shortcuts import render, redirect
from .forms import UserCreationForm, StudentForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm
# Create your views here.


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
        login_form = LoginForm(request, request.POST)
        if login_form.is_valid():
            print(login_form.cleaned_data)
            email = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print('Username not found')
        else:
            print('Username does not exist')
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login_signup_form.html', {'form': login_form} )