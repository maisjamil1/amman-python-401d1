from django.db import models
from django.urls import reverse

# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=64)
    eater = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('snacks')
        return reverse('snack_details', args=[str(self.id)])
