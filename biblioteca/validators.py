from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_year(value):
    year = timezone.now().year
    if value < 1400 or value > year:
        raise ValidationError(
            f"o ano deve ser entre 1400 e {year}"
        )
def validate_paginas(value):
    if value:
        if value < 0 or value > 5000:
             raise ValidationError(
                     f"as paginas devem ser entre 0 e 5000"
                     )

def validate_image_size(value):
    MB = value.size/1024
    if MB > 1:
        return ValidationError(
                     f"a capa tem tamanho maximo de 1MB"
                     )

