from django.contrib import admin
from .models import Livro, Autor, Category
# Register your models here.
@admin.register(Livro)
class Livros(admin.ModelAdmin):
    list_display= ['titulo', "ano_publicado", "disponivel"]
    search_fields= ['titulo', 'autores_temp']
    list_filter = ['disponivel', 'category']
    filter_horizontal = ["category", 'autores_temp']

# class ChoiceInLineBooks(admin.TabularInline):
#     model = Livro
#     extra = 1

# @admin.register(Autor)
# class Autores(admin.ModelAdmin):
#     inlines = [ChoiceInLineBooks]

#admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Category)