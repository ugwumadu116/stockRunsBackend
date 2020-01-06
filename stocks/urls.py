from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url


router = routers.DefaultRouter()
router.register('', views.StocksViews, basename="stocks" )

urlpatterns = [
    # path('', include(router.urls)),
    url(r'^joel/$', views.MyStockFileView.as_view(), name='file-upload'),
]
