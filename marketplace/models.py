from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

class Game(models.Model):
    """ Represents a single game """
    title = models.CharField(max_length=settings.GAME_TITLE_MAX_LENGTH, unique=True, help_text='The title of your game.')
    price = models.CharField(max_length=settings.PRICE_MAX_LENGTH, help_text="The price of your game.")
    slug = models.CharField(max_length=settings.GAME_TITLE_MAX_LENGTH, blank=True, editable=False,
                            help_text="Unique URL path to access this game. Generated by the system.")
    description = models.TextField(help_text="Write your game's description here.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a game (/my-new-game-page). """
        path_components = {'slug': self.slug}
        return reverse('game-detail-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Game, self).save(*args, **kwargs)