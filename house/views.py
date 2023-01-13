from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import views
from .permissions import IsOwnerOrReadOnly

from .models import House
from .serializers import HouseSerializer

import json

class HouseViewSet(viewsets.ModelViewSet):

    queryset = House.objects.filter(is_published=True)
    serializer_class = HouseSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
  

    def list(self,request,*args,**kwargs):
        data = HouseSerializer(self.queryset,many=True)
        response = Response(data.data)
        return response


    def retrieve(self,request,*args,**kwargs):
       pk:int = kwargs.get('pk')
       # print(published)
       house = House.objects.get(pk = pk)
       data = HouseSerializer(house)
       return Response(data.data)


      

 