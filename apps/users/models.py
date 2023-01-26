from django.db import models
from apps.users.utils import countries, others
from apps.countries.models import CountryModel
from apps.bioma.models import BiomeModel

class UserModel(models.Model):

   
    name = models.CharField(max_length=50, verbose_name = 'your name is?')
    last_name = models.CharField(max_length=50, verbose_name = 'and last name?')
    country = models.ForeignKey(CountryModel, on_delete=models.DO_NOTHING, related_name="users")
    biomes = models.ForeignKey(BiomeModel, on_delete=models.DO_NOTHING, verbose_name = 'places u like to travel')
    companies = models.CharField(max_length=50, choices=others.COMPANIES_CHOISES, verbose_name = 'how do you travel?')
    traveling_frequency = models.CharField(max_length=20, choices=others.TRAVEL_FREQUENCY, verbose_name='how often u take a trip?')