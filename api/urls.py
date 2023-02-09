from django.urls import path, include
from rest_framework import routers
from .views import PersonaList,UserViewSet, GroupViewSet

urlpatterns = [
    path('persona/',PersonaList.as_view(), name = 'persona_list'),
    path('users/',UserViewSet.as_view({'get': 'list'}), name = 'user_list'),
    path('groups/',GroupViewSet.as_view({'get': 'list'}), name = 'groups_list'),
]

