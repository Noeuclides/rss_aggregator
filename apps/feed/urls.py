from django.urls import path

from apps.feed.views import (PropertyDelete, PropertyList,
                                 PropertyOwnerList, PropertyRegister,
                                 PropertyUpdate, CompanyRegister)

urlpatterns = [
    path('list', PropertyList.as_view(), name='properties'),
    path('detail/<int:pk>', PropertyOwnerList.as_view(), name='owner_properties'),
    path('delete/<int:pk>', PropertyDelete.as_view(), name='feed_delete'),
    path('register', PropertyRegister.as_view(), name='register_feed'),
]
