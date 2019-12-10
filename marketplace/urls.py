from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-game', views.submit_game, name='submit game'),
    path('search', views.search, name='search'),
    path('game', views.game_detail, name='individual game detail'),
]