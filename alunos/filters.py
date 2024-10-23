import django_filters
from .models import Aluno

class AlunoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains', label="Nome contém")  # Filtro por nome que contenha a string
    matricula = django_filters.CharFilter(lookup_expr='exact')  # Filtro por matrícula exata
    idade = django_filters.NumberFilter()  # Filtro por idade exata
    email = django_filters.CharFilter(lookup_expr='icontains', label="E-mail contém") #Filtro por email que contenha a string

    class Meta:
        model = Aluno
        fields = ['nome','idade','email','matricula']
