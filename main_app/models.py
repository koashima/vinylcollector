from django.db import models

class Vinyl(models.Model): 
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    r_date = models.IntegerField()

    def __str__(self):
        return self.name

# vinyls = [ 
#     Vinyl('Abbey Road', 'rock', 'literally classic', 1969),
#     Vinyl('something1', 'rap', 'literally classic', 2000),
#     Vinyl('2something', 'alternative', 'literally classic', 2001),
# ]


