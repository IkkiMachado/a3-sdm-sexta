from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pagamentos'

router = routers.DefaultRouter()
router.register('', views.PagamentoViewSet, basename='pagamentos')

urlpatterns = [
    path('', include(router.urls) )
]