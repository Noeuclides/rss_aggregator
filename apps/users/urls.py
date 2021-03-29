from django.urls import path
from apps.users.views import Login, UserRegister, user_logout

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', user_logout, name='logout'),
    path('register', UserRegister.as_view(), name='register'),
]
