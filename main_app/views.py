from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Vinyl, Listening
from . forms import ListeningForm

def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

class VinylList(ListView):
    model = Vinyl
    
    def get_queryset(self):
        return Vinyl.objects.all()

def vinyl_detail(request, pk):
    vinyl = Vinyl.objects.get(id=pk)
    listening_form = ListeningForm()
    return render(request, 'main_app/vinyl_detail.html', {
        'vinyl' : vinyl,
        'listening_form': listening_form 
    })

def add_listening(request, pk):
    form = ListeningForm(request.POST)

    if form.is_valid():
        new_listening = form.save(commit=False)
        new_listening.vinyl_id = pk
        new_listening.save()    
    return redirect('vinyls_detail',)

class VinylCreate(CreateView):
    model = Vinyl
    fields = '__all__'

class VinylUpdate(UpdateView):
    model = Vinyl
    fields = '__all__'

class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls/'