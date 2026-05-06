from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'peliculas', views.PeliculaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.PeliculaListView.as_view(), name='pelicula-lista'),
    path('peliculas/nueva/', views.PeliculaCreateView.as_view(), name='pelicula-crear'),
    path('peliculas/<int:pk>/', views.PeliculaDetailView.as_view(), name='pelicula-detalle'),
    path('peliculas/<int:pk>/editar/', views.PeliculaUpdateView.as_view(), name='pelicula-editar'),
    path('peliculas/<int:pk>/eliminar/', views.PeliculaDeleteView.as_view(), name='pelicula-eliminar'),
]
