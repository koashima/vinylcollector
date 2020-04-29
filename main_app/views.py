from django.shortcuts import render
from django.views.generic import ListView
from . models import Vinyl

def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

class VinylList(ListView):
    model = Vinyl
    
    def get_queryset(self):
        return Vinyl.objects.all()


def vinyls_details(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    return render(request, 'vinyls/detail.html', { 'vinyl' : vinyl })