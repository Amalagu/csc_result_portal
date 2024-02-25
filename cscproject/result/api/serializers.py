from rest_framework import serializers
from result.models import RegisteredCourse, Result
from accounts.models import Student, User
from course.models import Course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['code']


class StudentSerializer(serializers.ModelSerializer):
    student = UserSerializer(many=False)
    class Meta:
        model = Student
        fields = ['student',]

class RegisteredCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False)
    class Meta:
        model = RegisteredCourse
        fields = ['course', 'grade']




class ResultSerializer(serializers.ModelSerializer):
    registeredcourses = serializers.SerializerMethodField()
    offeredcourses = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()

    class Meta:
        model = Result
        fields = ['student', 'registeredcourses', 'offeredcourses', 'tnu', 'tgp', 'cummulative_tgp', 'cummulative_tnu', 'gpa', 'cgpa']

    def get_registeredcourses(self, obj):
        registeredcourses = obj.registeredcourse_set.all()
        serializer = RegisteredCourseSerializer(registeredcourses, many=True)
        return serializer.data

    def get_offeredcourses(self, obj):
        offered_courses = obj.registeredcourse_set.values_list('course__code', flat=True)
        return list(offered_courses)
    
    def get_student(self, obj):
        student = obj.student.student.get_full_name
        return student



""" class ResultSerializer(serializers.ModelSerializer):
    registeredcourses = serializers.SerializerMethodField()
    offeredcourses = serializers.SerializerMethodField()
    student = StudentSerializer(many=False)

    class Meta:
        model = Result
        fields = ['student', 'registeredcourses', 'offeredcourses']

    def get_registeredcourses(self, obj):
        registeredcourses = obj.registeredcourse_set.all()
        serializer = RegisteredCourseSerializer(registeredcourses, many=True)
        return serializer.data

    def get_offeredcourses(self, obj):
        offered_courses = obj.registeredcourse_set.values_list('course__code', flat=True)
        return list(offered_courses)
 """
"""IF EVER YOU DECIDE TO USE THE SERIALIZER ABOVE, REMEMBER TO CHANGE THE TAG IN ADVISOR-SEMESTER-RESULT-SHEET.HTML
TO <td>{{studentdata.student.student.last_name}}</td> FROM THE CURRENT <td>{{studentdata.student}}</td>"""
