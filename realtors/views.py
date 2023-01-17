from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerilizer

class RealtorListView(ListAPIView):
	permission_classes = (permissions.AllowAny,)
	queryset = Realtor.objects.all()
	serializer_class = RealtorSerilizer
	pagination_class = None

	def list(self,request):
		print("from list method",self.queryset)



class RealtorView(RetrieveAPIView):
	queryset = Realtor.objects.all()
	serializer_class = RealtorSerilizer
	lookup_field = 'email'
	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		# print(instance.realtor_orders.all())
		serializer = self.get_serializer(instance)
		return Response(serializer.data)
	


class TopSellerView(ListAPIView):
	permission_classes = (permissions.AllowAny,)
	queryset = Realtor.objects.filter(top_seller = True)
	serializer_class = RealtorSerilizer
	pagination_class = None
