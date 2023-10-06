from django.db import models


# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    episodes = models.CharField(max_length=100)
    rating = models.CharField(max_length=30)
    members = models.IntegerField()

    def __str__(self):
        return self.name