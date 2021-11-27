from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase

from groups.models import Group, JoinGroupRequest
from accounts.models import User

class GroupModelTest(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="user",
            password="12345678",
        )
        
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + refresh.access_token)

        self.new_group = Group.objects.create(
            leader=1,
            name='new_group'
        )

        self.name_group = 'group_test'

        self.group = {
            "leader":self.user,
            "name": self.name_group
        }

        self.update_name_group = 'group_test'

        self.updated_group = {
            "name": self.update_name_group
        }

    def user_can_create_a_group(self):
        response = self.client.post("/api/groups/", self.group, format="json")

        self.assertEqual(response.status_code, 201)

    def user_can_update_a_group(self):
        group = self.client.post("/api/groups/", self.group, format="json")
        
        response = self.client.put(f"/api/groups/{group.id}", self.updated_group, format="json")
        
        self.assertEqual(response.status_code, 200)

    def user_can_delete_a_group(self):
        group = self.client.post("/api/groups/", self.group, format="json")

        response = self.client.delete(f"/api/groups/{group.id}")
        
        self.assertEqual(response.status_code, 204)

    def user_can_request_to_join_in_a_group(self):
        new_request = {'group_id':self.new_group.id, 'user_id':self.user.id}
        
        response = self.client.post(f"/api/groups/{self.new_group}/subscription/", new_request, format='json') 

        self.assertEqual(response.status_code, 201)

    def leader_can_accept_a_join_request(self):
        new_join_request = {'group_id':self.new_group.id, 'user_id':self.user.id}

        response = self.client.post(f"/api/groups/{self.new_group}/accept_member/", new_join_request, format='json') 

        self.assertEqual(response.status_code, 201)



