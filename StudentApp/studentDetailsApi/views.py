from django.shortcuts import render
from rest_framework.decorators import api_view

from exceptions.custom_exception import InvalidRequestException
from studentDetailsApi.models import StudentTShirtDetails
from rest_framework.response import Response
from rest_framework import status

from studentDetailsApi.serializers import StudentTShirtDetailsSerializers

# Create your views here.


@api_view(['GET', 'POST'])
def students_list(request):
    """List all students details"""
    try:
        if request.method == 'GET':
            students = StudentTShirtDetails.objects.all()
            serializer = StudentTShirtDetailsSerializers(students, many=True)
            return Response(serializer.data)
    except StudentTShirtDetails.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def student_create(request):
    """ Add new student details """
    if request.method == 'POST':
        serializer = StudentTShirtDetailsSerializers(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise InvalidRequestException
        except InvalidRequestException as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def student_detail(request, pk):
    """Get individual student detail"""
    try:
        student = StudentTShirtDetails.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = StudentTShirtDetailsSerializers(student)
            return Response(serializer.data)

    except StudentTShirtDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def student_detail_update(request, pk):
    """Update individual student detail"""
    try:
        student = StudentTShirtDetails.objects.get(pk=pk)
        if request.method == 'PUT':
            serializer = StudentTShirtDetailsSerializers(student, request.data)
            try:
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    raise InvalidRequestException
            except InvalidRequestException as e:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except StudentTShirtDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def student_detail_delete(request, pk):
    """ Delete student details"""
    try:
        student = StudentTShirtDetails.objects.get(pk=pk)
        if request.method == 'DELETE':
            student.delete()
            return Response(status=status.HTTP_301_MOVED_PERMANENTLY)
    except StudentTShirtDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
