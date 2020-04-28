from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Vinyl: 
    def __init__(self, name, genre, description, r_date):
        self.name = name
        self.genre = genre
        self.description = description
        self.r_date = r_date

vinyls = [ 
    Vinyl('Abbey Road', 'rock', 'literally classic', 1969),
    Vinyl('something1', 'rap', 'literally classic', 2000),
    Vinyl('2something', 'alternative', 'literally classic', 2001),
]


def home(request): 
    return HttpResponse('<h1>HELLO VINYL COLLECTOR</h1>')

def about(request): 
    return render(request, 'about.html')

def vinyls_index(request):
    return render(request, 'vinyls/index.html', {'vinyls' : vinyls}) 