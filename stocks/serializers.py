from rest_framework import serializers
from .models import StockStore


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockStore
        fields = ('symbol', 'value', 'volume', 'trades', 'change_percent', 'change', 'close', 'low', 'high', 'open_value', 'prev_close', 'date')
        
