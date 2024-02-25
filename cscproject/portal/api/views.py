from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer
from course.models import Course
from django.db.models import Sum, F
from portal.models import Session, Semester
from django.contrib.auth.decorators import login_required




class CourseDetailsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        results = Course.objects.get(id=id)
        serializer = CourseSerializer(results)
        print('CALLED COURSE DETAILS API VIEW')
        return Response(serializer.data, status=status.HTTP_200_OK)