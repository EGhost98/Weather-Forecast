from django.test import TestCase, Client

class TemplateTest(TestCase):
    def test_index_template(self):
        client = Client()
        response = client.get('/index')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast/index.html')
