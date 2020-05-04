from django.db import models
from django.urls import reverse

class Contributor(models.Model):
    artist = models.CharField(max_length=100)

    def __str__(self): 
        return self.artist

    def get_absolute_url(self):
        return reverse('contributors_detail', kwargs={'pk': self.id})


class Vinyl(models.Model): 
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    r_date = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('vinyls_detail', kwargs={'pk': self.id})

EXTENTS = (
    ('B', 'Barely'),
    ('P', 'Partial'),
    ('C', 'Complete')
)

class Listening(models.Model):
    date = models.DateField('listening date')
    extent = models.CharField(
        max_length=1,
        choices=EXTENTS,
        default=EXTENTS[0][0]
    )
    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_extent_display()} on {self.date}"

    class Meta:
        ordering = ['-date']