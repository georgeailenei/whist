from rest_framework.serializers import ModelSerializer

from userauth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")
