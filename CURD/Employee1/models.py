from django.db import models

class EmployeeProfile(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    local_address=models.CharField(max_length=100)
    perma_address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.EmailField()
    father=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    mother=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)

    def __str__(self):
        return self.name


