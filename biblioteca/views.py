from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Autor
from .forms import AutorForm, LivroForm

# Create your views here.
def home(request):
    livros = Livro.objects.all()
    return render(request, "index.html", {"livros": livros})

def autor(request, id):
    escritor = get_object_or_404(Autor, id=id)

    return render(request, "detalhes.html", {"autor": escritor, "livros": escritor.books.all()})

def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)

        if form.is_valid():
            autor = form.save()
            return redirect('detalhes', id=autor.pk)

    else:
        form = AutorForm()

    return render(request, 'criar_autor.html', {'form': form})

def criar_livro(request):
    if request.method == 'POST':
            form = LivroForm(request.POST)
    
            if form.is_valid():
                autor = form.save()
                return redirect("index")
    else:
        form = LivroForm()

    return render(request, "livro.html", {"form": form, "edited": False})

def editar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    if request.method == 'POST':
            form = LivroForm(request.POST, instance=livro)
    
            if form.is_valid():
                livro = form.save()
                print(livro)
                return redirect("detalhes", id=livro.autores_temp.all()[0].id)
    else:
        form = LivroForm(instance=livro)
    return render(request, "livro.html", {"form": form, "edited": True})