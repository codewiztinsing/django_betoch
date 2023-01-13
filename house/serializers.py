from rest_framework import serializers
from .models import House



class HouseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = House
        fields = [
            'category',
            'title',
            'slug',
            'is_published',
            'description',
            'price',
            'oldPrice',
            'avgRating',
            'get_image',
            #'images',
            'thumbnail',
            'date_added',
            'owner',
            'images'
            ]