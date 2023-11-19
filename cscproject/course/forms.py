from django.forms import ModelForm, Form
from .models import Course
from django import forms
from portal.models import Semester



class CourseModelForm(ModelForm):
    level_list = (
        ('100 LEVEL', '100 LEVEL'),
        ('200 LEVEL', '200 LEVEL' ),
        ('300 LEVEL', '300 LEVEL'),
        ('400 LEVEL', '400 LEVEL'),
        ('500 LEVEL', '500 LEVEL')
    )

    unit_list = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (6, 6)
)
    code = forms.CharField(label='Course Code', max_length=7, required=True, widget=forms.TextInput(attrs={'class': 'input', 'id': 'course_code', 'required': True}))
    title = forms.CharField(label='Course Title', max_length=140, required=True, widget=forms.TextInput(attrs={'class': 'input', 'id': 'course_title', 'required': True}))
    unit = forms.ChoiceField( label='Course Unit', required=True, choices=unit_list,  widget=forms.Select(attrs={'class': 'input', 'id': 'phone_number', 'required': True}))
    semester = forms.ModelChoiceField(queryset=Semester.objects.all(), label='Semester', widget=forms.Select(attrs={'class': 'input', 'id': 'class_set', 'required': True}))
    iselective = forms.BooleanField(label='This is an Elective Course', required=True)
    level = forms.ChoiceField(label='Course Level', required=True, choices=level_list,  widget=forms.Select(attrs={'class': 'input', 'id': 'elective', 'required': True}))

    class Meta:
        model = Course
        fields = '__all__'
    
    """ def save(self, commit=True):
        code = self.cleaned_data.get('code')
        title = self.cleaned_data.get('title')
        unit = int(self.cleaned_data.get('unit'))
        semester = self.cleaned_data.get('semester')
        iselective = self.cleaned_data.get('iselective')
        level = self.cleaned_data.get('level')
        course = Course.objects.create(code=code, title=title, unit=unit, semester=semester, iselective=iselective, level=level)
        course.save() """