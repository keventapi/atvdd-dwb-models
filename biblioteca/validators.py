from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_year(value):
    year = timezone.now().year
    if 1400 < value or value > year:
        raise ValidationError(
            f"o ano deve ser entre 1400 e {year}"
        )
def validate_paginas(value):
    if value:
        if value < 0 or value > 5000:
             raise ValidationError(
                     f"as paginas devem ser entre 0 e 5000"
                     )