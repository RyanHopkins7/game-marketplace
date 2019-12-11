from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from marketplace.models import Game
from api.serializers import GameSerializer

class GameList(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(RetrieveDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
