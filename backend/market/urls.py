from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarketDataViewSet

router = DefaultRouter()
router.register(r'marketdata', MarketDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
