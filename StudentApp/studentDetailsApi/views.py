from rest_framework.permissions import IsAuthenticated, IsAdminUser

from studentDetailsApi.models import StudentTShirtDetails
from rest_framework import generics, permissions

from studentDetailsApi.serializers import StudentTShirtDetailsSerializers


# Create your views here.

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of profile to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class StudentsRecordsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers


class StudentRecordCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StudentRecord(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers


class StudentRecordUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StudentRecordDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers
