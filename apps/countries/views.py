from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from apps.countries.serializers import CountrySerializer
from apps.countries.models import CountryModel

class CountriesViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    serializer_class = CountrySerializer
    queryset = CountryModel.objects.all()

    
