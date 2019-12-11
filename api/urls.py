from django.urls import path
from api.views import GameList, GameDetail

urlpatterns = [
    path('games/', GameList.as_view(), name='game_list'),
    path('games/<int:pk>', GameDetail.as_view(), name='game_detail')
]
