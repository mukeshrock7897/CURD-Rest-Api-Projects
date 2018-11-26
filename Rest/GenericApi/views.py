import django_filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from .models import Employee
from .serializers import EmployeeSerializer,LoginSerializer,UserSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BasicAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.views import APIView
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import filters
from rest_framework.filters import OrderingFilter,SearchFilter

from rest_framework.pagination import PageNumberPagination

#this is used only for pagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

class BillingRecordsView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = StandardResultsSetPagination


#this create the employee list by generic methods ways


class GenericEmployeeList(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field='id'
    authentication_classes = (TokenAuthentication,SessionAuthentication,BasicAuthentication,BaseAuthentication)
    permission_classes = (IsAuthenticated,IsAdminUser)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('company','city')




    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


    def put(self,request,id=None):
        return self.update(request,id)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)


    def delete(self,request,id=None):
        return self.destroy(request,id)

    def perform_destroy(self, instance):
        instance.save(created_by=self.request.user)

#this is only for login


class LoginView(APIView):

    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        login(request,user)
        token,created=Token.objects.get_or_create(user=user)
        return Response({'token':token.key},status=status.HTTP_200_OK)


#this is used for logout

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    def post(self,request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


#this is used to show all list of user  & also can search , filter according to your need

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends=(DjangoFilterBackend,OrderingFilter,SearchFilter)
    filter_fields=('is_active','username')
    ordering_fields=('username','is_active')
    
    search_fields = ('username', 'email')

    #def get_queryset(self):
     #   queryset = User.objects.all()
      #  active = self.request.query_params.get('is_active', '')
       # if active:
        #    if active == "False":
         #       active = False
          #  elif active == "True":
           #     active = True
            #else:
             #   return queryset
            #return queryset.filter(is_active=active)
        #return queryset




#-----------------------------------Viewsets and Router using-------------------------------------------------------------------------------

from rest_framework import viewsets


#class EmployeeView(viewsets.ModelViewSet):
 #   serializer_class = EmployeeSerializer
  #  queryset = Employee.objects.all()
   # lookup_field = 'id'



