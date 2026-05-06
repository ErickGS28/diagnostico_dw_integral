from rest_framework import viewsets
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pelicula
from .serializers import PeliculaSerializer


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'peliculas/lista.html'
    context_object_name = 'peliculas'


class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'peliculas/detalle.html'
    context_object_name = 'pelicula'


class PeliculaCreateView(CreateView):
    model = Pelicula
    template_name = 'peliculas/formulario.html'
    fields = ['titulo', 'director', 'anio', 'genero', 'sinopsis', 'duracion_minutos']
    success_url = reverse_lazy('pelicula-lista')


class PeliculaUpdateView(UpdateView):
    model = Pelicula
    template_name = 'peliculas/formulario.html'
    fields = ['titulo', 'director', 'anio', 'genero', 'sinopsis', 'duracion_minutos']
    success_url = reverse_lazy('pelicula-lista')


class PeliculaDeleteView(DeleteView):
    model = Pelicula
    template_name = 'peliculas/confirmar_eliminar.html'
    success_url = reverse_lazy('pelicula-lista')
