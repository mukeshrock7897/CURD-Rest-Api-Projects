from django.urls import path
from Employee1 import views

urlpatterns=[
    path('index/',views.EmployeeCreation),
    path('read/',views.EmployeeRead),


]