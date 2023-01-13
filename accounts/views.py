from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpView(APIView):

	def post(self,request,format = None):
		data = self.request.data
		name = data['username']
		email = data['email']
		password = data['password']
		password2 = data['password2']

		if password == password2:
			if User.objects.filter(email = email).exists():
				return Response({'error':'Email Already Exists'})
			else:
				user = User.objects.create_user(email = email,name=name,password=password)
				user.save()
				return Response({'message':'user created successfullly'})
		else:
			return Response({'message':'password does\'t match'})
