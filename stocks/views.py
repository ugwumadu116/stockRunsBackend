from django.shortcuts import render
from rest_framework import viewsets
from .models import StockStore
from .serializers import StockSerializer

class StocksViews(viewsets.ModelViewSet):
    queryset = StockStore.objects.all()
    serializer_class = StockSerializer
