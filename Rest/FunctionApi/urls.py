from django.urls import path
from FunctionApi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[


    path('items/',views.product_list),
    path('items/<int:id>',views.product_detail),
    path('user/',views.user_list),

    path('user/<int:id>', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)