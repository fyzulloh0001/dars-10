
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
from django.shortcuts import render
from homeapp.models import Page
from django.urls import reverse_lazy

# Create your views here.
class BlockListView(ListView):
    model=Page
    template_name='home.html'
    
class BlockDetailView(DetailView):
    model=Page
    template_name='detailview.html'
    
class BlockCreateView(CreateView):
    model=Page
    template_name='createview.html'
    fields=['title','author','text']
class BlockUpdateView(UpdateView):
    model=Page
    template_name='updateview.html'
    fields=['title','text']
    
class BlockDeleteView(DeleteView):
    model=Page
    template_name='deleteview.html'
    
  
    success_url=reverse_lazy('home')
    
    
    