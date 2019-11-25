from django.contrib import admin
from django.urls import path, include
from . import views


from django.urls import path





urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include('stocks.urls')),
    path('admin/', admin.site.urls),
]
