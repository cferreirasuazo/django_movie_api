from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet, 'movie')

urlpatterns = [
    path ('', include(router.urls)),
]