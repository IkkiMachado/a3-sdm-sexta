from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'itemreserva'

router = routers.DefaultRouter()
router.register('', views.ItemReservaViewSet, basename='itemreserva')

urlpatterns = [
    path('', include(router.urls) )
]