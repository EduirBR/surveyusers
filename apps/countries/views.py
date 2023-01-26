from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.countries.serializers import CountrySerializer
from apps.countries.models import CountryModel
from rest_framework.response import Response


class CountriesViewSet(ReadOnlyModelViewSet):
    serializer_class = CountrySerializer
    queryset = CountryModel.objects.all()

    
