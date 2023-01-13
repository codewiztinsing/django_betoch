from rest_framework import serializers
from .models import Listing



class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'title',
            'city',
            'address',
            'state',
            'home_type',
            'sale_type',
            'bed_rooms',
            'bath_rooms',
            'sqrt',
            'slug',
            'published',
            'description',
            'price',
            'get_image',
            # 'images',
            'date_added',
            ]





class ListingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'