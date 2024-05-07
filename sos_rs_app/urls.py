from django.urls import path
from .genericviews import UserAPIView, UsersAPIView, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users'),
    path('users/<int:pk>', UserAPIView.as_view(), name='user'),
] 
