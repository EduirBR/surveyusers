import uuid
from django.db import models

class CountryModel(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150, verbose_name = 'Pais', unique=True)
    official = models.CharField(max_length=150)
    capital = models.CharField(max_length=150, blank=True, verbose_name = 'Capital')
    continent = models.CharField(max_length=150, verbose_name = 'Continente')
    languages = models.CharField(max_length=150, verbose_name = 'Idioma Principal')
    currency = models.CharField(max_length=150, blank=True, verbose_name = 'Moneda')
    flagSVG = models.CharField(max_length=150)
    flagPNG = models.CharField(max_length=150)
    