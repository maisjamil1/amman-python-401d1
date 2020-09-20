from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class SnacksTest(SimpleTestCase):
    def test_home_page_status_code(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code # Request to the application
        # assert expected == actual
        self.assertEquals(expected, actual)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'snacks-home.html'
        self.assertTemplateUsed(response, actual)
