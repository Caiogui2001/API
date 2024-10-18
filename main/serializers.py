from rest_framework import serializers
from .models import Item, Funcionario

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['nome', 'descricao']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['nome_funcionario', 'idade', 'cargo']