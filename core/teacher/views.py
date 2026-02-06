from django.http import Http404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from core.teacher.models import Teacher, BankInfo
from core.teacher.serializers import TeacherSerializer

class TeachersView(APIView):
    serializer_class = TeacherSerializer

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = self.serializer_class(teachers, many=True)
        return Response(serializer.data)

class TeacherProfileView(APIView):
    serializer_class = TeacherSerializer

    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        teacher = self.get_object(pk)
        serializer = self.serializer_class(teacher)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = self.get_object(pk)
        serializer = self.serializer_class(teacher, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
