from django.urls import path
from . import views
from marketplace.views import GameDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-game/', views.GameCreateView.as_view(), name='submit-game-page'),
    path('search/', views.search, name='search-page'),
    path('game/', views.game_detail, name='game'),
    path('<str:slug>/', GameDetailView.as_view(), name='game-detail-page'),
]