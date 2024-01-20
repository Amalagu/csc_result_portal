from rest_framework import serializers
from result.models import RegisteredCourse, Result
from accounts.models import Student, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class StudentSerializer(serializers.ModelSerializer):
    student = UserSerializer(many=False)
    class Meta:
        model = Student
        fields = ['student',]

class RegisteredCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredCourse
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    registeredcourses = serializers.SerializerMethodField()
    student = StudentSerializer(many=False)
    class Meta:
        model= Result
        fields = ['student', 'gpa', 'cgpa', 'student_class', 'registeredcourses']

    def get_registeredcourses(self, obj):
        registeredcourses = obj.registeredcourse_set.all()
        serializer = RegisteredCourseSerializer(registeredcourses, many=True)
        return serializer.data


