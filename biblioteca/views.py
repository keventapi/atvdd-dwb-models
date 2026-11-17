from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from .models import Livro, Autor
from .forms import AutorForm, LivroForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)



class HomeListView(ListView):
    model = Livro
    template_name = "index.html"
    context_object_name = "livros"
    ordering = ["titulo"]


class LivroDetailView(DetailView):
    model = Livro
    template_name = "livro_detalhes.html"
    context_object_name = "livro"

class AutorDetailView(DetailView):
    model = Autor
    template_name = "detalhes.html"
    context_object_name = "autor"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["livros"] = self.object.books.all()
        return context


class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = "criar_autor.html"

    def get_success_url(self):
        return reverse("detalhes", kwargs={"id": self.object.pk})


class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm  # Troque para LivroModelForm se você renomeou a classe em forms.py
    template_name = "livro.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edited"] = False
        return context


class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = "livro.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edited"] = True
        return context

class LivroDeleteView(DeleteView):
    model = Livro
    template_name = "livro_confirm_delete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("index")

class SobreTemplateView(TemplateView):
    template_name = "sobre.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_livros"] = Livro.objects.count()
        context["livros_disponiveis"] = Livro.objects.filter(disponivel=True).count()
        return context


