from django import forms
from .models import Autor, Livro
from django.utils import timezone

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name', 'nationality']

        labels = {
            'name': 'Nome',
            'nationality': 'Nacionalidade',
        }

        error_messages = {
            'name': {
                'required': 'O nome do autor é obrigatório.',
            }
        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro

        fields = "__all__"

    def clean(self):
        super().clean()
        titulo: str = self.cleaned_data.get("titulo")
        if not titulo:
            self.add_error("titulo", "titulo deve ser uma str")

        normalized_titulo = titulo.strip()
        if len(normalized_titulo) <= 3:
            self.add_error("titulo", "titulo deve possuir pelo menos 3 caracteres")

        self.cleaned_data["titulo"] = normalized_titulo

        ano_publicado = self.cleaned_data.get("ano_publicado")
        now = timezone.now()
        year = now.year
        if ano_publicado > year:
            self.add_error("ano_publicado", "o ano deve ser o atual ou anterior, não aceita data futura")
             
        return self.cleaned_data