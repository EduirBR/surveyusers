from rest_framework.serializers import ModelSerializer
from apps.users.models import UserModel

class UserSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'