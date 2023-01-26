import json
from django.core.management.base import BaseCommand
from apps.countries.models import CountryModel
from apps.countries.serializers import CountrySerializer
class Command(BaseCommand):

    help = 'seedcountries'

    def handle(self, *args, **options):

        with open('apps/countries/seeder/commands/.json') as file:
            data = json.load(file)

        for i in range(0, len(data["data"]), 1):
            countries_serializers = CountrySerializer(
                data=data["data"][i])
            if countries_serializers.is_valid():
                countries_serializers.save()
