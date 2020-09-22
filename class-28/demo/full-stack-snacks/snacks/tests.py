from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Snack
from django.urls import reverse
# Create your tests here.

class SnackTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Ghafri',
            email='ghafri@gmail.com',
            password='password'
        )

        self.snack = Snack.objects.create(
            name='oranges',
            description='Vitmain C',
            eater=self.user
        )

    def test_snack_list_view(self):
        response = self.client.get(reverse('snacks'))
        self.assertEqual(response.status_code, 200)

    def test_snack_details_view(self):
        response = self.client.get(reverse('snack_details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_update_view(self):
        response = self.client.post(reverse('snack_update', args='1'), {
            'name': 'chips',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'chips')
