from django.shortcuts import render
from rest_framework import viewsets
from .models import StockStore
from .serializers import StockSerializer, MyStockFileSerializer

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class StocksViews(viewsets.ModelViewSet):
    queryset = StockStore.objects.all()
    serializer_class = StockSerializer


class MyStockFileView(APIView):
	parser_classes = (MultiPartParser, FormParser)
	def post(self, request, *args, **kwargs):    
		file_serializer = MyStockFileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
