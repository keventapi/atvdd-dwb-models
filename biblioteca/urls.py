"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import HomeListView, AutorDetailView, AutorCreateView, LivroCreateView, LivroDeleteView, LivroDetailView, LivroUpdateView, SobreTemplateView
from django.urls import path

urlpatterns = [
    path("", HomeListView.as_view(), name="index"),
    path("livro/<int:pk>/", LivroDetailView.as_view(), name="livro_detalhes"),
    path("autor/<int:id>/", AutorDetailView.as_view(), name="detalhes"),
    path("autor/novo/", AutorCreateView.as_view(), name="criar_autor"),
    path("livro/novo/", LivroCreateView.as_view(), name="criar_livro"),
    path("livro/<int:id>/editar/", LivroUpdateView.as_view(), name="editar_livro"),
    path("livro/<int:id>/excluir/", LivroDeleteView.as_view(), name="excluir_livro"),
    path("sobre/", SobreTemplateView.as_view(), name="sobre"),
]
