""" from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, Student
from django.forms import Form
from django import forms
from portal.models import StudentClass

forms.Form

class StudentForm(Form):
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=15, label='PhoneNumber')
    first_name = forms.CharField(max_length=30, label="Firstname")
    last_name = forms.CharField(max_length=30, label="Lastname")
    class_set = forms.CharField(max_length=9, label="Class Set")
    registeration_number = forms.CharField(max_length=11)
    password1 = forms.CharField(max_length=30, label='Password')
    password2 = forms.CharField(max_length=30, label='Password Confirmation')

    def save(self, commit=True):
        student_class = StudentClass.objects.get(class_set=self.cleaned_data.get('class_set'))  or None
        user = User.objects.create(
            email=self.cleaned_data.get('email'),
            phone_number = self.cleaned_data.get('phone_number'),
            first_name = self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            password = self.cleaned_data.get('password1')
        )
        user.save()
        student = Student.objects.create(
            student=user, 
            registeration_number=self.cleaned_data.get('registeration_number'),
            student_class = student_class
        )
        student.save()
        return student
     """


from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, Student
from django.forms import Form, ModelForm
from django import forms
from portal.models import StudentClass

from accounts.models import User

session_list = [
    ('2022/2023', '2022/2023'),
    ('2023/2024', '2023/2024')
]





class StudentForm(UserCreationForm):
    #email = forms.EmailField(label='Email',  required=True)
    #phone_number = forms.CharField(max_length=15, label='PhoneNumber')
    #first_name = forms.CharField(max_length=30, label="Firstname", required=True)
    #last_name = forms.CharField(max_length=30, label="Lastname",  required=True)
    #class_set = forms.ModelChoiceField(queryset=StudentClass.objects.all())
    #registeration_number = forms.CharField(max_length=11)
    email = forms.EmailField(label='Email Address', required=True, widget=forms.EmailInput(attrs={'class': 'input', 'id': 'email', 'required': True}))
    phone_number = forms.CharField(max_length=15, label='Phone Number', widget=forms.TextInput(attrs={'class': 'input', 'id': 'phone_number', 'required': True}))
    first_name = forms.CharField(max_length=30, label="First Name", required=True, widget=forms.TextInput(attrs={'class': 'input', 'id': 'first_name', 'required': True}))
    last_name = forms.CharField(max_length=30, label="Last Name", required=True, widget=forms.TextInput(attrs={'class': 'input', 'id': 'last_name', 'required': True}))
    class_set = forms.ModelChoiceField(label='Class Set', queryset=StudentClass.objects.all(), widget=forms.Select(attrs={'class': 'input', 'id': 'class_set', 'required': True}))
    registeration_number = forms.CharField(label='Registeration Number', max_length=11, widget=forms.TextInput(attrs={'class': 'input', 'id': 'registeration_number', 'required': True}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'password1', 'required': True}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'password2', 'required': True}))
    """ class_set = forms.CharField(
        max_length=9,
        label="Class Set",
        widget=forms.Select(choices=session_list)
    )   #If you uncomment this, you will have to uncomment line that queries and retrieves student class instance """
    

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.set_password(self.cleaned_data.get('password1'))  # Set the password correctly
        user.save()
        #student_class = StudentClass.objects.get(class_set=self.cleaned_data.get('class_set')) or None     #If you uncomment this, you will have to uncomment line that receives class_set as charfield or as choice list
        student_class = self.cleaned_data.get('class_set') or None
        student = Student.objects.create(
            student=user,
            registeration_number=self.cleaned_data.get('registeration_number'),
            student_class=student_class
        )
        return student





class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "other_names", "last_name", "phone_number")

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "other_names", "last_name", "phone_number")

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'input', 'type':'text', 'id': 'username', 'required': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'password', 'required': True}))






class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'other_names', 'address', 'email', 'phone_number']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input rounded w-full', 'name':'firstName', 'id':'first-name'}),
            'last_name': forms.TextInput(attrs={'class': 'input rounded w-full', 'name':'lastName', 'id':'last-name'}),
            'other_names': forms.TextInput(attrs={'class': 'input rounded w-full', 'name':'middleName', 'id':'middle-name'}),
            'email': forms.EmailInput(attrs={'class': 'input rounded w-full', 'name':'email', 'id':'email'}),
            'address': forms.TextInput(attrs={'class': 'input rounded w-full', 'name':'homeAddress', 'id':'home-address'}),
            'phone_number': forms.TextInput(attrs={'class': 'input rounded w-full', 'name':'phone', 'id':'phone'}),
        }

    """ def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super(UserModelForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'input rounded w-full', 'name':'firstName', 'id':'first-name', 'value': instance.first_name}) """
        
        


        



