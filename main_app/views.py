from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Vinyl

def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

class VinylList(ListView):
    model = Vinyl
    
    def get_queryset(self):
        return Vinyl.objects.all()

class VinylDetail(DetailView):
    model = Vinyl

class VinylCreate(CreateView):
    model = Vinyl
    fields = '__all__'

class VinylUpdate(UpdateView):
    model = Vinyl
    fields = '__all__'

class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls/'