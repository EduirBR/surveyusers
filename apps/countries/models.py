import uuid
from django.db import models

class CountryModel(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, verbose_name = 'Pais')
    english_name = models.CharField(max_length=50, verbose_name = 'Pais en ingles')
    capital = models.CharField(max_length=50, verbose_name = 'Capital')
    continent = models.CharField(max_length=50, verbose_name = 'Continente')
    main_language = models.CharField(max_length=50, verbose_name = 'Idioma Principal')
    currency = models.CharField(max_length=50, verbose_name = 'Moneda')
    currency_symbol = models.CharField(max_length=50, verbose_name = 'Simbolo de Moneda')