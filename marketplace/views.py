from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def submit_game(request):
    return render(request, 'sell.html')

def search(request):
    return render(request, 'search.html')

def game_detail(request):
    return render(request, 'individual_game.html')