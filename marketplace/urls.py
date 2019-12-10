from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-game', views.submit_game, name='submit-game-page'),
    path('search', views.search, name='search-page'),
    path('game', views.game_detail, name='game-detail-page'),
]