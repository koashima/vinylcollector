from django.db import models
from django.urls import reverse
class Vinyl(models.Model): 
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    r_date = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_abolute_url(self):
        return reverse('detail', kwargs={'vinyl_id': self.id})