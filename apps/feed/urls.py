from django.urls import path

from apps.feed.views.views import UserFeed, FeedRegister, FeedDetail

urlpatterns = [
    path('detail/<int:pk>', UserFeed.as_view(), name='user_feed'),
    path('feed/<int:pk>', FeedDetail.as_view(), name='feed'),
    path('register', FeedRegister.as_view(), name='feed_register'),
]
