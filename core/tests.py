from django.test import TestCase


class IndexViewTest(TestCase):
    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_json_content(self):
        response = self.client.get('/')
        self.assertEqual(response.json(), {'message': 'Hello CI/CD World!'})
