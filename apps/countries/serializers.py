from rest_framework.serializers import ModelSerializer
from apps.countries.models import CountryModel
from apps.users.serializers import UserSerializer

class CountryUserSerializer(ModelSerializer):
    users = UserSerializer(
        many=True, read_only=True)

    class Meta:
        model = CountryModel
        fields = '__all__'
        
class CountrySerializer(ModelSerializer):
 
    class Meta:
        model = CountryModel
        fields = '__all__'

class CountryHTMLSerializer(ModelSerializer):
    
    class Meta:
        model = CountryModel
        fields = '__all__'
        
    def to_representation(self, instance):
        data={
            'name':instance.name,
            'uuid':instance.uuid
        }
        return data