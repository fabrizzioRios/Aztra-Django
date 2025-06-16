from rest_framework import serializers
from tasks.models import Tarea


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'


class CambiarEstadoSerializer(serializers.Serializer):
    estado = serializers.ChoiceField(choices=Tarea.ESTADOS)
