from django.db import models

# Create your models here.
class Food(models.Model):
    """docstring for Food."""
    full_name = models.CharField(max_length=200)
    color =  models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
