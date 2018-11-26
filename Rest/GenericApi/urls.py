from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from GenericApi.views import *

#this is used for router

from rest_framework.routers import DefaultRouter

#router=DefaultRouter()
#router.register('employees',EmployeeView)

#this is used for Schema Views Details

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="Example API")


urlpatterns=[

    path('schema/',schema_view),
    path('page/',BillingRecordsView.as_view()),
    path('user/',UserListView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('employees/',GenericEmployeeList.as_view()),
    path('employees/<int:id>/',GenericEmployeeList.as_view()),

 #   path('',include(router.urls)),

]

urlpatterns = format_suffix_patterns(urlpatterns)