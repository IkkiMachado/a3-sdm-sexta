from .models import VeiculoAcessorio
from rest_framework import serializers

class VeiculoacessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeiculoAcessorio
        fields = '__all__'