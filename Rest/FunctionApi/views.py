from django.shortcuts import render,HttpResponse,Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.reverse import reverse


@api_view(['GET','POST'])
def product_list(request, format=None):
    if request.method=="GET":
        obj=Product.objects.all()
        serializer=ProductSerializer(obj,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def product_detail(request,id,format=None):
    try:
        obj=Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=ProductSerializer(obj)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=ProductSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method=="DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def user_list(request):
    if request.method=="GET":
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET','PUT'])
def user_detail(request,id):
    try:
        obj=User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=UserSerializer(obj)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=UserSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

