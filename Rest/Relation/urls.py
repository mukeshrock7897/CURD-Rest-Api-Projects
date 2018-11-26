from django.urls import path

from Relation import views

from Relation.views import *

urlpatterns=[
    path('albums/',AlbumView.as_view()),
    path('albums/<int:id>',AlbumView.as_view()),


]