from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Vinyl, Listening, Contributor
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
    contributors_vinyl_doesnt_have = Contributor.objects.exclude(id__in = vinyl.contributors.all().values_list('id'))
    listening_form = ListeningForm()
    return render(request, 'main_app/vinyl_detail.html', {
        'vinyl' : vinyl,
        'listening_form': listening_form,
        'contributors': contributors_vinyl_doesnt_have
    })

def add_listening(request, pk):
    form = ListeningForm(request.POST)

    if form.is_valid():
        new_listening = form.save(commit=False)
        new_listening.vinyl_id = pk
        new_listening.save()    
    return redirect('vinyls_detail', pk=pk)

class VinylCreate(CreateView):
    model = Vinyl
    fields = '__all__'

class VinylUpdate(UpdateView):
    model = Vinyl
    fields = '__all__'

class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls/'

class ContributorList(ListView):
    model = Contributor

class ContributorDetail(DetailView):
    model = Contributor    

def assoc_contributor(request, vinyl_id, contributor_id):
    Vinyl.objects.get(id=vinyl_id).contributors.add(contributor_id)
    return redirect('vinyls_detail', pk=vinyl_id) 