from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from accounts.models import User
from .models import Group

class UserGroupSerializer(ModelSerializer):
      class Meta:
        model = User
        fields = ['id', 'username']

class GroupSerializer(ModelSerializer):
    leader = UserGroupSerializer(read_only=True)
    class Meta:
        model = Group
        exclude = ['users']
    
    def create(self, validated_data):     
        user = self.initial_data.pop('user')   
        
        group = Group.objects.create(**self.initial_data) 
        
        group.users.add(user, through_defaults={'is_admin': True})

        return group

class JoinGroupSerilizer(serializers.Serializer):
    user = UserGroupSerializer(read_only=True)
