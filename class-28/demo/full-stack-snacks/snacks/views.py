from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Snack
# Create your views here.

# list, details, create, update, delete

class SnacksView(ListView):
    template_name = 'snacks.html'
    model = Snack

class SnackDetailsView(DetailView):
    template_name = 'snack_details.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['name', 'eater', 'description']

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['name', 'eater', 'description']
    # success_url = reverse_lazy('snacks')

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snacks')
