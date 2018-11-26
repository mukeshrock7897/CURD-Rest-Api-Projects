from django.urls import path
from ForignRelationShip import views

urlpatterns=[
    path('detail/',views.EmployeeDetail),
    path('id/<int:id>',views.EmployeeID),
    path('personal/',views.personal),

]


