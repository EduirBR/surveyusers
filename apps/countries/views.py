from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.countries.serializers import CountrySerializer, CountryHTMLSerializer
from apps.countries.models import CountryModel
from rest_framework.response import Response


class CountriesViewSet(ReadOnlyModelViewSet):
    serializer_class = CountrySerializer
    queryset = CountryModel.objects.all()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk, *args, **kwargs):
        if pk == 'HTML':
            countries = self.queryset
            countries_serializer = CountryHTMLSerializer(countries, many=True)
            return Response(countries_serializer.data)
        return super().retrieve(request, *args, **kwargs)

# class CHTMLViewSet(ReadOnlyModelViewSet):
#     serializer_class = CountryHTMLSerializer
#     queryset = CountryModel.objects.all()

    
