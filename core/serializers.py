from rest_framework import serializers
from .models import CoreFilmes


class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreFilmes
        fields = ['id', 'nome', 'mes', 'ano', 'genero', 'tipo', 'receita']
