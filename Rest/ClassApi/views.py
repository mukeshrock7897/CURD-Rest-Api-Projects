from django.shortcuts import render
from django.views.decorators.vary import vary_on_cookie

from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class EmployeeList(APIView):

    #@method_decorator(cache_page(60*60*1))
    #@method_decorator(vary_on_cookie)
    def get(self,request, format=None):

        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data)

    def post(self,request, format=None):

        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class EmployeeDetail(APIView):

    def get_object(self,id):
        try:
            return Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):

        employee=self.get_object(id)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_302_FOUND)


    def put(self,request,id):
        employee=self.get_object(id)
        serializer=EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)


    def delete(self,request,id):
        employee=self.get_object(id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#--------------------------------------------------------------------------------------------------------------------------

