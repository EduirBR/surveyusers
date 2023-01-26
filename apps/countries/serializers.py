from rest_framework.serializers import ModelSerializer
from apps.countries.models import CountryModel
from apps.users.serializers import UserSerializer

class CountrySerializer(ModelSerializer):

    users = UserSerializer(many=True)

    class Meta:
        model = CountryModel
        fields = '__all__'