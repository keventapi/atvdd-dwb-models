from django.shortcuts import render, get_object_or_404
from .models import Livro, Autor
# Create your views here.
def home(request):
    livros = Livro.objects.all()
    return render(request, "index.html", {"livros": livros})

def autor(request, id):
    escritor = get_object_or_404(Autor, id=id)

    return render(request, "detalhes.html", {"autor": escritor, "livros": escritor.books.all()})