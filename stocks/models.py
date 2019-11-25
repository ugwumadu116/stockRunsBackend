from django.db import models
from djmoney.models.fields import MoneyField
from datetime import datetime 


class StockStore(models.Model):
    symbol = models.CharField(max_length=60)
    value = models.IntegerField(null=True)
    model = MoneyField(max_digits=60,decimal_places=2, default_currency='NGN', null=True)
    volume = models.IntegerField(null=True)
    trades = models.IntegerField( null=True)
    change_percent = models.FloatField(null=True)
    change = models.FloatField(null=True)
    close = models.FloatField(null=True)
    low = models.FloatField(null=True)
    high = models.FloatField(null=True)
    open_value = models.FloatField(null=True)
    prev_close = models.FloatField(null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.symbol
