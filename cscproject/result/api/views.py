from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResultSerializer, RegisteredCourseSerializer
from result.models import Result, RegisteredCourse
from django.db.models import Sum, F
from portal.models import Session, Semester


class ResultDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




