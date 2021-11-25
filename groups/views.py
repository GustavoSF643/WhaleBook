from rest_framework import viewsets
from .models import Group, JoinGroupRequest
from .serializers import GroupSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class GroupModelView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(methods=['post'], detail=True)
    def subscription(self, request, *args, **kwargs):
        JoinGroupRequest.objects.create(user_id='', group_id='')

        return Response({'message':'Permission requested'}, status=status.HTTP_201_CREATED)