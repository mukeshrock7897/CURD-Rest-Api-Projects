
from rest_framework import serializers

from .models import Product
from django.contrib.auth.models import  User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','name','description','price')



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields="__all__"



