from django.shortcuts import render
from . models import Vinyl

def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def vinyls_index(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyls/index.html', { 'vinyls' : vinyls }) 

def vinyls_details(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    return render(request, 'vinyls/detail.html', { 'vinyl' : vinyl })