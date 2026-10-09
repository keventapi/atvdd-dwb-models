from django.contrib import admin
from .models import Livro, Autor, Category
# Register your models here.
@admin.register(Livro)
class Livros(admin.ModelAdmin):
    list_display= ['titulo', "autor", "ano_publicado", "disponivel"]
    search_fields= ['titulo', 'autor']
    list_filter = ['disponivel', 'category']
    filter_horizontal = ["category"]

class ChoiceInLineBooks(admin.TabularInline):
    model = Livro
    extra = 1

@admin.register(Autor)
class Autores(admin.ModelAdmin):
    inlines = [ChoiceInLineBooks]

admin.site.register(Category)