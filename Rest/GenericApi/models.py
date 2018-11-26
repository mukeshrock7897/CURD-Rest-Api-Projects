from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.first_name


