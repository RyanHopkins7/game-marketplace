from django import forms
from marketplace.models import Game

class GameForm(forms.ModelForm):
    """ Render and process a form based on the Game model. """
    class Meta:
        model = Game
        fields = ['title', 'price', 'image_url', 'description']

    model = Game