from django.shortcuts import render
from .models import Livro
# Create your views here.
def home(request):
    livros = Livro.objects.all()
    return render(request, "index.html", {"livros": livros})