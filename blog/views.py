from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Simulation


class HomePageView(ListView):
    model = Simulation
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Simulation
    template_name = 'post_detail.html'

    def detail(request, pk):
        post = get_object_or_404(Simulation, pk=pk)
        return render(request, 'post_detail.html', {'post': post})


class BlogCreateView(CreateView):
    model = Simulation
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Simulation
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Simulation
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
