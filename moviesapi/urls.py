from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import MoviesViewSet, yearmovies, topmovies, searchmovies

router = routers.DefaultRouter()
router.register('movies', MoviesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('yearmovies/<int:idano>', yearmovies),
    path('topmovies/<int:idano>', topmovies),
    path('searchmovies/<str:nomesearch>', searchmovies)
]
