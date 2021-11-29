from accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from utils.permissions import IsLeaderOfGroupOrReadOnly
from django.core.exceptions import ObjectDoesNotExist


from .models import Group, GroupGoals, JoinGroupRequest
from .serializers import GroupGoalSeriliazer, GroupSerializer, UserGroupSerializer, JoinGroupSerializer


class GroupView(viewsets.ModelViewSet):
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

        return Response({'Message':'Created a request to join the group'}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, permission_classes=[IsLeaderOfGroupOrReadOnly], url_path='accept_member/(?P<user_id>[^/.]+)')
    def accept_member(self, request, *args, **kwargs):
        group = self.get_object()
        
        new_member = get_object_or_404(User, id=kwargs.get('user_id')) 

        user_request = JoinGroupRequest.objects.filter(group_id=group, user_id=new_member)
        
        if user_request:
            user_request.delete()

        group.users.add(new_member)
    
        return Response({'Message':'New member added'}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def request_users(self, request, *args, **kwargs):
        group = self.get_object()

        new_members_request = JoinGroupRequest.objects.filter(group_id=group.id)

        serializer = JoinGroupSerializer(new_members_request, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=True)
    def members(self, request, *args, **kwargs):
        group = self.get_object()

        members = group.users.all()
        
        serializer = UserGroupSerializer(members, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class GroupGoalsView(viewsets.ModelViewSet):
    permission_classes = [IsLeaderOfGroupOrReadOnly]

    queryset = GroupGoals.objects.all()
    serializer_class = GroupGoalSeriliazer

    lookup_field = 'id'

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        
        return queryset.filter(group_id=self.kwargs.get('pk'))

    def create(self, request, *args, **kwargs):      
        group = Group.objects.get(id=kwargs['pk'])
        
        request.data['owner'] = request.user

        request.data['group'] = group
        
        return super().create(request, *args, **kwargs)

    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated])
    def join(self, request, *args, **kwargs):
        group = get_object_or_404(Group, id=kwargs.get('pk'))

        group_goal = self.get_object()
        
        new_member = request.user

        try:
            group.users.get(id=new_member.id)

            group_goal.members.add(new_member)

            return Response({'Message':'Associated with a goal'}, status=status.HTTP_200_OK)
            
        except ObjectDoesNotExist:
            return Response({'Error':'User is not in the group'}, status=status.HTTP_403_FORBIDDEN)
    
    @action(methods=['delete'], detail=True, permission_classes=[IsAuthenticated])
    def leave(self, request, *args, **kwargs):
        group_goal = self.get_object()

        member = group_goal.members.get(id=request.user.id)

        group_goal.members.remove(member)

        return Response({'Message':'Disabled to a goal'}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated])
    def members(self, request, *args, **kwargs):
        group_goal = self.get_object()

        members = group_goal.members.all()

        serializer = UserGroupSerializer(members, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated])
    def update_status(self, request, *args, **kwargs):
        group_goal = self.get_object()
        
        user_read_status = group_goal.groupgoalsusers_set.get(user_id=request.user)

        user_read_status.completed = True

        user_read_status.save()

        return Response({'Message':'Updated reading status'}, status=status.HTTP_200_OK)
