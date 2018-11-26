from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.forms import modelform_factory,modelformset_factory,inlineformset_factory
from ForignRelationShip.models import Employee,Company,Person

def EmployeeDetail(request):
    employee=Employee.objects.all()
    return render(request,'ForignRelationShip/detail.html',{'employee':employee})


def EmployeeID(request,id):
    try:
        employee=Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        raise Http404("This ID is Not Exist......")
    return render(request,'ForignRelationShip/id.html',{'employee':employee})




def personal(request):
    PersonForm=modelform_factory(Person,fields=('first_name','last_name'))
    if request.method=="POST":
        formset=PersonForm(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponse("Your Form Filled SuccessFully")
    else:
        formset=PersonForm()
    return render(request,'ForignRelationShip/personal.html',{'formset':formset})




#from django.core.mail import BadHeaderError, send_mail
#from django.http import HttpResponse, HttpResponseRedirect




#def send_email(request):
#	subject = request.POST.get('subject', 'Nothing')
#	message = request.POST.get('message', 'This came From Views')
#	from_email = request.POST.get('from_email', 'mukeshrock7897@gmail.com')

#if subject and message and from_email:
 #   try:
  #      send_mail(subject, message, from_email, ['mukeshpro97@gmail.com'])
   # except BadHeaderError:
    #    return HttpResponse('Invalid header found.')

    #return HttpResponseRedirect('/Relation/detail/')
#else:
 #   return HttpResponse("Failure")

