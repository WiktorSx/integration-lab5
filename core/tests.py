from django.test import TestCase

class IndexViewTest(TestCase):
    # Test 1: Sprawdza czy endpoint zwraca status 200
    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Test 2: Sprawdza czy endpoint zwraca poprawna wiadomosc
    def test_index_json_content(self):
        response = self.client.get('/')
        self.assertEqual(response.json(), {'message': 'Hello CI/CD World!'})