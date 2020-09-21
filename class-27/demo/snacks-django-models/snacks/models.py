from django.db import models

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    rank = models.IntegerField(default=1)
    eater = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    # Eater should be a user in our app
    def __str__(self):
        return self.name
