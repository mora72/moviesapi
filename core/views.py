# from requests import Response
from rest_framework import viewsets
from .models import CoreFilmes
from .serializers import FilmesSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = CoreFilmes.objects.filter(ano=2020).order_by('-receita')
    serializer_class = FilmesSerializer


@csrf_exempt
def yearmovies(request, idano):
    if request.method == 'GET':
        queryset = CoreFilmes.objects.filter(ano=idano).order_by('-receita')
        serializer = FilmesSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def topmovies(request, idano):
    if request.method == 'GET':
        if idano != 0:
            queryset = CoreFilmes.objects.filter(ano=idano).order_by('-receita')[:10]
        else:
            queryset = CoreFilmes.objects.all().order_by('-receita')[:10]
        serializer = FilmesSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def searchmovies(request, nomesearch):
    if request.method == 'GET':
        queryset = CoreFilmes.objects.filter(nome__icontains=nomesearch).order_by('nome')
        serializer = FilmesSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
