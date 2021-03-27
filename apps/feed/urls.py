from django.urls import path

from apps.feed.views import (UserFeed, FeedRegister)

urlpatterns = [
    path('detail/<int:pk>', UserFeed.as_view(), name='user_feed'),
    path('register', FeedRegister.as_view(), name='feed_register'),
]
