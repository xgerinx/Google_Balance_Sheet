from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import BalanceSheetSerializer
from .models import BalanceSheet


class BalanceSheetViewSet(ReadOnlyModelViewSet):
    queryset = BalanceSheet.objects.all()
    serializer_class = BalanceSheetSerializer
