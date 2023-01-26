from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SkipField
from apps.users.models import UserModel
from collections import OrderedDict
from rest_framework.relations import PKOnlyObject


class UserSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'
 
    def to_representation(self, instance):
        ret =  {
        "id": instance.id,
        "name": instance.name,
        "last_name": instance.last_name,
        "biomes": instance.biomes.name,
        "companies": instance.companies,
        "traveling_frequency": instance.traveling_frequency,
        "country": instance.country.name
        }
        
        return ret
