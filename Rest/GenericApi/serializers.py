from rest_framework import serializers
from .models import Employee
from rest_framework import exceptions
from django.contrib.auth import authenticate
from django.contrib.auth.models import  User



class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Employee

        fields="__all__"


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):
        username=data.get('username','')
        password=data.get('password','')

        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data['user']=user

                else:
                    raise exceptions.ValidationError("User is Deactivated Currently....")
            else:
                raise exceptions.ValidationError("Unable to login with given Credentials.....")
        else:
            raise exceptions.ValidationError("Please Provide Correct Username and Password......")
        return data





class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model=User
        fields=[

            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'is_superuser'
        ]



