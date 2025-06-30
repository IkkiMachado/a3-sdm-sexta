from .models import ItemReserva
from rest_framework import serializers

class ItemReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReserva
        fields = '__all__'