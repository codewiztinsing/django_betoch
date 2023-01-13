from django.urls import path
from .views import UserList,UserDetail,UserListCreate
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('',csrf_exempt(UserListCreate.as_view())),
    path('<int:pk>/',UserDetail.as_view(),name="user-detail")
]
