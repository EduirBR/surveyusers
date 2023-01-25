from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from apps.users.serializers import UserSerializer
from apps.users.models import UserModel

class UserView(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

class UserREAD(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()