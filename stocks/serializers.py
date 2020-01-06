from rest_framework import serializers
from .models import StockStore, MyStockFile


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockStore
        fields = ('symbol', 'value', 'volume', 'trades', 'change_percent', 'change', 'close', 'low', 'high', 'open_value', 'prev_close', 'date')
        
class MyStockFileSerializer(serializers.ModelSerializer):

	class Meta:
            model = MyStockFile
            fields = ('file', 'uploaded_at')


