from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, SeatViewSet

router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'seats', SeatViewSet, basename='seat')
urlpatterns = [
    path('', include(router.urls)),
]