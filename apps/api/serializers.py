from rest_framework import serializers
from usuarios.models import Usuario
from visitantes.models import Visitante
from porteiros.models import Porteiro

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'


class PorteiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Porteiro
        fields = '__all__'

