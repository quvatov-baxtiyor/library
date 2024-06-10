from rest_framework import routers
from django.urls import path,include
from .views import BookViewSet, UserViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('',include(router.urls)),
]