from django.shortcuts import render,HttpResponse,redirect,Http404,HttpResponseRedirect

from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q
from django.contrib import messages

def EmployeeCreation(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request,'Employee/index.html',{'form':form})



def ReadEmployee(request):
    employee=Employee.objects.all()

    return render(request,'Employee/Read.html',{'employee':employee})


def EditEmployee(request,id):
    try:
        employee=Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        raise Http404("Employee Does't Exist With This ID")
    return render(request,'Employee/Edit.html',{'employee':employee})


def UpdateEmployee(request,id):
    employee=Employee.objects.get(pk=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/Employee/show')
    return render(request,"Employee/Edit.html",{'employee':employee})


def DeleteEmployee(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/Employee/show')

def search(request):
    if request.method=="POST":
        srch=request.POST['srh']
        if srch:
            match=Employee.objects.filter(Q(eid__contains=srch)|Q(ename__icontains=srch))

            if match:
                return render(request,'Employee/search.html',{'sr':match})

            else:
                messages.error(request,"No Result Found........")
        else:
            return HttpResponseRedirect('/Employee/search/')
    return render(request,'Employee/search.html')

