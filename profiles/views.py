from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileDetail(APIView):
    def get(self,request):
        owner = self.request.user
        print(owner)
        profiles = Profile.objects.all()
        profie_data = ProfileSerializer(profiles,many=True)
        return Response(profie_data.data)

    def post(self,request,format=None):
        data = request.data
        owner = request.user.username
        first_name = data['first_name']
        last_name = data['last_name']
        avatar = data['avatar']

        profile = Profile.objects.create(
            owner=data['owner'],
            first_name=first_name,
            last_name=last_name,
            avatar = "http://localhost:8000"+avatar)
        profile.save()


        return Response({
            "message":"profile created"
            },status.HTTP_200_OK)



class ProfileUpdate(APIView):
    def get(self,request,format=None):
       return Response({
            "message":"profile detail"
            })

    def post(self,request,format=None):
        return Response({
            "message":"profile detail"
            })