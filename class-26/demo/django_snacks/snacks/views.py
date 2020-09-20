from django.shortcuts import render
# Create your views here.


# Step 2: Create home view
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'snacks-home.html' # Add a template

class AboutView(TemplateView):
    template_name = 'snacks-about.html'
