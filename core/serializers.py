from rest_framework import serializers
from core.models import EquityStockWatch


class EquityStockWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquityStockWatch
        fields = "__all__"

