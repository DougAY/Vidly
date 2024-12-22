from django.db import models
from django.utils import timezone

# Create your models here.
class genre(models.Model):
    name = models.CharField(max_length=255)


class movies(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(genre,on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)