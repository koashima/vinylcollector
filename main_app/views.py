from django.shortcuts import render

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
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def vinyls_index(request):
    return render(request, 'vinyls/index.html', {'vinyls' : vinyls}) 