from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.generics import RetrieveDestroyAPIView
from marketplace.models import Game
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from marketplace.forms import GameForm

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def game_detail(request):
    return render(request, 'individual_game.html')

class GameCreateView(CreateView):
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
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'individual_game.html')