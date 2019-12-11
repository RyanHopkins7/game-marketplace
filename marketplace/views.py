from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.generics import RetrieveDestroyAPIView
from marketplace.models import Game
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from marketplace.forms import GameForm
from django.views.generic.list import ListView

def index(request):
    return render(request, 'index.html')

class GameListView(ListView):
    """ Renders a list of all Games. """
    model = Game

    def get(self, request):
        """ GET a list of Games. """
        games = self.get_queryset().all()
        return render(request, 'index.html', {
          'games': games
        })

class GameCreateView(CreateView):
    """ Renders form to list a new Game. """
    def get(self, request, *args, **kwargs):
        context = {'form': GameForm()}
        return render(request, 'sell.html', context)

    def post(self, request, *args, **kwargs):
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            return HttpResponseRedirect('/'+game.slug)
        return render(request, 'sell.html', {'form': form})

class GameDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Game

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        game = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'individual_game.html', {'game': game})