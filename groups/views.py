from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from accounts.models import User
from .models import Group, JoinGroupRequest
from .serializers import GroupSerializer, JoinGroupSerilizer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class GroupModelView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(methods=['post'], detail=True)
    def subscription(self, request, *args, **kwargs):
        group = self.get_object()
   
        JoinGroupRequest.objects.create(user_id=kwargs['pk'], group_id=group)

        return Response({'Message':'Created request to join the group'}, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True)
    def accept_member(self, request, *args, **kwargs):
        group = self.get_object()

        new_member = get_object_or_404(User, id=kwargs['pk'])

        group.users.add(new_member)
    
        return Response({'Message':'New member added'}, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False)
    def new_members(self, request, *args, **kwargs):
        group = self.get_object()

        new_members_request = JoinGroupRequest.objects.filter(group_id=group.id)

        serializer = JoinGroupSerilizer(new_members_request, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    
