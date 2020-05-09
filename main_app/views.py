from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Vinyl, Listening, Contributor
from . forms import ListeningForm


def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

class VinylList(LoginRequiredMixin, ListView):
    model = Vinyl
    
    def get_queryset(self):
        return Vinyl.objects.filter(user=self.request.user)


@login_required
def vinyl_detail(request, pk):
    vinyl = Vinyl.objects.get(id=pk)
    contributors_vinyl_doesnt_have = Contributor.objects.exclude(id__in = vinyl.contributors.all().values_list('id'))
    listening_form = ListeningForm()
    return render(request, 'main_app/vinyl_detail.html', {
        'vinyl' : vinyl,
        'listening_form': listening_form,
        'contributors': contributors_vinyl_doesnt_have
    })

@login_required
def add_listening(request, pk):
    form = ListeningForm(request.POST)

    if form.is_valid():
        new_listening = form.save(commit=False)
        new_listening.vinyl_id = pk
        new_listening.save()    
    return redirect('vinyls_detail', pk=pk)

class VinylCreate(LoginRequiredMixin, CreateView):
    model = Vinyl
    fields = ['name', 'genre', 'description', 'release_Date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VinylUpdate(LoginRequiredMixin, UpdateView):
    model = Vinyl
    fields = '__all__'

class VinylDelete(LoginRequiredMixin, DeleteView):
    model = Vinyl
    success_url = '/vinyls/'

class ContributorList(LoginRequiredMixin, ListView):
    model = Contributor

class ContributorDetail(LoginRequiredMixin, DetailView):
    model = Contributor

class ContributorCreate(LoginRequiredMixin, CreateView):
    model = Contributor
    fields = '__all__'
    
class ContributorUpdate(LoginRequiredMixin, UpdateView):
    model = Contributor
    fields = ['artist']

class ContributorDelete(LoginRequiredMixin, DeleteView):
  model = Contributor
  success_url = '/contributors/'

@login_required
def assoc_contributor(request, vinyl_id, contributor_id):
    Vinyl.objects.get(id=vinyl_id).contributors.add(contributor_id)
    return redirect('vinyls_detail', pk=vinyl_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vinyls_index')
    else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)