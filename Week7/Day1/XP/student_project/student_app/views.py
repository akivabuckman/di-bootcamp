from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


# Create a student_list view for handling GET and POST requests
# Handle GET request by retrieving all Student objects and serializing them
# Handle POST request by saving data from the request and serializing it if valid

class StudentListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def put(self, request, pk, *args, **kwargs):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk, *args, **kwargs):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(HTTP_204_NO_CONTENT)