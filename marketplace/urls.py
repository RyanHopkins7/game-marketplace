from django.urls import path
from . import views
from marketplace.views import GameDetailView

urlpatterns = [
    path('', views.GameListView.as_view(), name='home'),
    path('submit-game/', views.GameCreateView.as_view(), name='submit-game-page'),
    path('<str:slug>/', GameDetailView.as_view(), name='game-detail-page'),
]