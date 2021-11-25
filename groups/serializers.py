from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Group

class GroupSerializer(ModelSerializer):
   
    class Meta:
        model = Group
        fields = '__all__'


class JoinGroupSerilizer(serializers.Serializer):
    ...
