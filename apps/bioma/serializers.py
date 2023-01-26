from rest_framework.serializers import ModelSerializer
from apps.bioma.models import BiomeModel

class BiomeSerializer(ModelSerializer):

    class Meta:
        model = BiomeModel
        fields = '__all__'