from django.shortcuts import render
from rest_framework import viewsets
from .models import Item, Funcionario
from .serializers import ItemSerializer, FuncionarioSerializer  # Import correto

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer  