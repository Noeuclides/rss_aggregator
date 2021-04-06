from django.urls import path

from apps.feed.views.views import UserFeed, FeedRegister, FeedDetail, FeedDelete

urlpatterns = [
    path('detail/<int:pk>', UserFeed.as_view(), name='user_feed'),
    path('feed/<int:pk>', FeedDetail.as_view(), name='feed'),
    path('delete_feed/<int:pk>', FeedDelete.as_view(), name='delete_feed'),
    path('register', FeedRegister.as_view(), name='feed_register'),
]
