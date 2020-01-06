from django.urls import path, include
from .controllers.stock_view import StocksViews
from rest_framework import routers
from django.conf.urls import url


router = routers.DefaultRouter()
router.register('', StocksViews, basename="stocks" )

urlpatterns = [
    path('', include(router.urls)),
]
