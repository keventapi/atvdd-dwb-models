from django import forms
from .models import Autor


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

        