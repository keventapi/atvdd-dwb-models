from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        verbose_name = "autor"
        verbose_name_plural = "autores"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}, {self.nationality}"

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="books")
    category = models.ManyToManyField(Category, blank=True, null=True)
    ano_publicado = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"titulo: {self.titulo} \n autor: {self.autor}. \n ano de publicação: {self.ano_publicado} \n dispnivel: {self.disponivel} \n categorias: {self.category}"
