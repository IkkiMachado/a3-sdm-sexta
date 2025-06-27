from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'acessorios'

router = routers.DefaultRouter()
router.register('', views.AcessorioViewSet, basename='acessorios')

urlpatterns = [
    path('', include(router.urls) )
]