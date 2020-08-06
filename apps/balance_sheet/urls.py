from django.urls import path, include
from rest_framework import routers

from .views import BalanceSheetViewSet

router = routers.SimpleRouter()
router.register('', BalanceSheetViewSet, basename='balance_sheet')

urlpatterns = [
    path('', include(router.urls)),
]
