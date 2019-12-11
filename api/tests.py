from django.test import TestCase

class TestAPI(TestCase):
    def test_api_listview(self):
        response = self.client.get('/api/games/')
        self.assertEquals(response.status_code, 200)
    
    def test_api_detailview(self):
        game_data = {'title': 'Test Title', 'price': '500$', 'image_url': 'Google.com', 'description': 'Test game'}
        response = self.client.post('/api/games/', game_data)
        self.assertEquals(response.status_code, 201)

        response = self.client.get('/api/games/1')
        self.assertEquals(response.status_code, 200)