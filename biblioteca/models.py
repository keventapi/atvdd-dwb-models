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
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f"{self.name}"

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autores_temp = models.ManyToManyField(Autor, related_name="books")
    category = models.ManyToManyField(Category, blank=True, null=True)
    ano_publicado = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        if self.autores_temp.count() < 1:
            raise ValueError("é necessario ter pelo menos um autor registrado")

        super().save(*args,**kwargs)

    def __str__(self):
        return f"titulo: {self.titulo} \n autor: {self.autores_temp.all()}. \n ano de publicação: {self.ano_publicado} \n dispnivel: {self.disponivel} \n categorias: {self.category}"
