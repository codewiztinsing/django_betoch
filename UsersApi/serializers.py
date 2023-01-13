from django.contrib.auth.models import User
from rest_framework import serializers
"""
 A user can access a poll or the list  of detail screen.
 Only an authenticated users can create a order.
 Only an authenticated user can create a submit house info.
 Authenticated users can't create orders  for their own house.
 Authenticated users can delete only polls they have created.
 Only an authenticated user can vote. Users can vote for other people’s polls.
To enable the access control, we need to add two more APIs
• API to create a user, we will call this endpoint /users/
• API to verify a user and get a token to identify them, we will call this endpoint /login/

"""
class UserSerializer(serializers.ModelSerializer):
    # houses = serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):

            user = User(
            email=validated_data['email'],
            username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user