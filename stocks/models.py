from django.db import models
from djmoney.models.fields import MoneyField
from datetime import datetime
import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage



class OverwriteStorage(FileSystemStorage):

    '''
    Muda o comportamento padrão do Django e o faz sobrescrever arquivos de
    mesmo nome que foram carregados pelo usuário ao invés de renomeá-los.
    '''
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

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


class MyStockFile(models.Model):
    file = models.FileField(u"mytest", blank=False, null=False,  upload_to=settings.MEDIA_ROOT, storage=OverwriteStorage())
    # file = models.FileField(blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)








# class Media(models.Model):
#     name = models.CharField(u"Nome", max_length=128))
#     media = models.FileField(u"Arquivo", upload_to=settings.MEDIA_DIR, storage=OverwriteStorage())
