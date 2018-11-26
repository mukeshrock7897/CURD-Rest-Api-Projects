from django.urls import path

from Employee import views

urlpatterns=[
    path('home/',views.EmployeeCreation),
    path('search/',views.search),
    path('show/',views.ReadEmployee),
    path('edit/<int:id>',views.EditEmployee),
    path('update/<int:id>',views.UpdateEmployee),
    path('delete/<int:id>',views.DeleteEmployee),

]