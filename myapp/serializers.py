from rest_framework import serializers
from .models import Setor, Pessoa

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
