from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator
from biblioteca import validators

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
    capa = models.ImageField(upload_to="capas/", validators=[validators.validate_image_size, FileExtensionValidator(["jpg", "jpeg", "png"])], null=True, blank=True)
    titulo = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    autores_temp = models.ManyToManyField(Autor, related_name="books")
    category = models.ManyToManyField(Category, blank=True, null=True)
    ano_publicado = models.IntegerField(validators=[validators.validate_year])
    paginas = models.IntegerField(validators=[validators.validate_paginas], null=True, blank=True)
    disponivel = models.BooleanField(default=True)
    isbn = models.CharField(max_length=13, validators=[MinLengthValidator(13)], null=True, blank=True)

    def __str__(self):
        return f"titulo: {self.titulo} \n autor: {self.autores_temp.all()}. \n ano de publicação: {self.ano_publicado} \n dispnivel: {self.disponivel} \n categorias: {self.category}"
