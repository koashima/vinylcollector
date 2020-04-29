from django.db import models

class Vinyl(models.Model): 
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    r_date = models.IntegerField()

    def __str__(self):
        return self.name
