from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'veiculos'

router = routers.DefaultRouter()
router.register('', views.VeiculoViewSet, basename='veiculos')

urlpatterns = [
    path('', include(router.urls) )
]