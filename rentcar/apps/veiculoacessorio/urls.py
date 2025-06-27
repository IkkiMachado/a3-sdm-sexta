from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'veiculoacessorio'

router = routers.DefaultRouter()
router.register('', views.VeiculoAcessorioViewSet, basename='veiculoacessorio')

urlpatterns = [
    path('', include(router.urls) )
]