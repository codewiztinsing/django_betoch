from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer,ListingDetailSerializer


class ListingsView(ListAPIView):
	queryset = Listing.objects.filter(published = True)
	serializer_class = ListingSerializer
	# permission_classes = (permissions.AllowAny)
	pagination_class = None



class ListingView(ListAPIView):
	queryset           = Listing.objects.filter(published = True)
	serializer_class   = ListingDetailSerializer
	# permission_classes = (permissions.AllowAny)
	lookup_field       = 'slug'



class SearchView(APIView):

	def post(self,request,format = None):
		
		permissions_classes = (permissions.AllowAny,)
		queryset = Listing.objects.filter(published = True)
		data   =  self.request.data

		# sale_type = data['sale_type']  
		# queryset = queryset.filter(sale_type__iexact = sale_type)

		home_type = data['home_type'] 
		city = data['city']  
		
		if home_type:
			queryset = queryset.filter(home_type = home_type) 

		if home_type and city:
			queryset = queryset.filter(home_type = home_type).filter(city = city) 

		

		# city = data['city']  
		# queryset = queryset.filter(city__iexact = city)  

		serialize = ListingSerializer(queryset,many = True)
		return Response(serialize.data) 
		





