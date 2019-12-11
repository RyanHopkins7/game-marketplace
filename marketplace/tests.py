from django.test import TestCase
from marketplace.models import Game
from marketplace.forms import GameForm
from django.http import HttpResponseRedirect

class TestViews(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_submit(self):
        response = self.client.get('/submit-game/')
        self.assertEqual(response.status_code, 200)

class TestModels(TestCase):
    def test_game(self):
        form = GameForm({'title': 'Test Title', 'price': '500$', 'image_url': 'Google.com', 'description': 'Test game'})
        self.assert_(form.is_valid())

        game = form.save(commit=False)
        game.save()

        self.assertEquals(game.slug, 'test-title')

        response = self.client.get('/'+game.slug+'/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Test Title')