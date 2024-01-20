from django.db import models

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=100)
    age_recommended = models.IntegerField()

    def __str__(self):
        return self.name

