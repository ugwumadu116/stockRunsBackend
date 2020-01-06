from django.shortcuts import render
from rest_framework import viewsets
from ..models.stock_model import StockStore
from ..serializers.stock_serializers import StockSerializer

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class StocksViews(viewsets.ModelViewSet):
    queryset = StockStore.objects.all()
    serializer_class = StockSerializer

