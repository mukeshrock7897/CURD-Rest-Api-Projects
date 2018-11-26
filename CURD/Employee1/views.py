from django.shortcuts import render,redirect,HttpResponse
from .forms import EmployeeForm
from .models import EmployeeProfile


def EmployeeCreation(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Record Saved Successfully")
    else:
        form=EmployeeForm()
    return render(request,'Employee1/Creation.html',{'form':form})


def EmployeeRead(request):
    employee=EmployeeProfile.objects.all()
    return render(request,'Employee1/Read.html',{'employee':employee})


