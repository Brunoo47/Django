from core.models import Ocorrencias
from rest_framework import serializers

class OcorrenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencias
        fields = '__all__'