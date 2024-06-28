from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pessoa, Setor
from .serializers import PessoaSerializer, SetorSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [IsAuthenticated]

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
    permission_classes = [IsAuthenticated]
    