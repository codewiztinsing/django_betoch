from django.urls import path
from .views import ProfileDetail,ProfileUpdate

urlpatterns = [
	path('',ProfileDetail.as_view(),name="profile-detail"),
	path('update/',ProfileUpdate.as_view(),name="profile-update")
]