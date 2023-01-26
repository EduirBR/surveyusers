from rest_framework.viewsets import ModelViewSet
from apps.bioma.models import BiomeModel
from apps.bioma.serializers import BiomeSerializer

class BiomeViewSet(ModelViewSet):
    queryset = BiomeModel.objects.all()
    serializer_class =BiomeSerializer
