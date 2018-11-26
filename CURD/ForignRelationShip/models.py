from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,verbose_name=Employee)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.position

#Creating the Custom Model Manager

class PersonManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().all()



class Person(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    persons=PersonManager()




class MyPerson(Person):

    class Meta:
        proxy=True





