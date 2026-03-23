from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SessionViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]