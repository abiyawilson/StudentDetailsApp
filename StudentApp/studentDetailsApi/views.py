
from studentDetailsApi.models import StudentTShirtDetails
from rest_framework import generics

from studentDetailsApi.serializers import StudentTShirtDetailsSerializers


# Create your views here.


class StudentsRecordsList(generics.ListAPIView):
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers


class StudentRecordCreate(generics.CreateAPIView):
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers


class StudentRecord(generics.RetrieveAPIView):
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers


class StudentRecordUpdate(generics.UpdateAPIView):
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers


class StudentRecordDelete(generics.DestroyAPIView):
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers


