from accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from utils.permissions import IsLeaderOfGroup

from .models import Group, JoinGroupRequest
from .serializers import GroupSerializer, JoinGroupSerilizer, UserGroupSerializer


class GroupModelView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['leader_id'] = request.auth['user_id']

        request.data['user'] = request.user

        return super().create(request, *args, **kwargs)
    
    @action(methods=['post'], detail=True)
    def subscription(self, request, *args, **kwargs):
        group = self.get_object()
   
        JoinGroupRequest.objects.create(user_id=request.user.id, group_id=group.id)

        return Response({'Message':'Created request to join the group'}, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True, permission_classes=[IsLeaderOfGroup])
    def accept_member(self, request, *args, **kwargs):
        group = self.get_object()

        new_member = get_object_or_404(User, id=request.data['new_member'])

        group.users.add(new_member)
    
        return Response({'Message':'New member added'}, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=True)
    def new_members(self, request, *args, **kwargs):
        group = self.get_object()

        new_members_request = JoinGroupRequest.objects.filter(group_id=group.id)

        serializer = JoinGroupSerilizer(new_members_request, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=True)
    def members(self, request, *args, **kwargs):
        group = self.get_object()

        members = group.users.all()
        
        serializer = UserGroupSerializer(members, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

