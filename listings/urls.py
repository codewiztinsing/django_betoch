from django.urls import path
from .views import ListingsView,ListingView,SearchView
urlpatterns = [
	path('',ListingsView.as_view(),name = 'listings'),
	path('<slug>',ListingView.as_view(),name = 'listing'),
	path('search/',SearchView.as_view(),name = 'listing'),
]