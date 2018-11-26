from django.shortcuts import render

from .serializer import AlbumSerializer,TrackSerializer

from .models import Album,Track

from rest_framework import status

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import generics

from rest_framework import mixins

class AlbumView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field='id'






    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)



    def put(self,request,id=None):
        return self.update(request,id)



    def delete(self,request,id=None):
        return self.destroy(request,id)



