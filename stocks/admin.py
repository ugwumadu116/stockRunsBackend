from django.contrib import admin

from django.contrib import admin
from .models.stock_model import StockStore


# Register your models here.
admin.site.register([StockStore])
