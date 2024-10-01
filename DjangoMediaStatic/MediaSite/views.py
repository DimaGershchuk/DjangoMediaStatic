from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import MyMedia
from .forms import MediaForm
from django.urls import reverse_lazy


class CreateMedia(CreateView):
    model = MyMedia
    template_name = 'create_media.html'
    form_class = MediaForm
    success_url = reverse_lazy('home')


class ListMedia(ListView):
    model = MyMedia
    template_name = 'home.html'


class MediaDetails(DetailView):
    model = MyMedia
    template_name = 'detail_media.html'




