from django.test import TestCase

from groups.models import Group, JoinGroupRequest
from accounts.models import User

class GroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.username = 'user'
        cls.password = '1234'

        cls.user = User.objects.create_user(
            username=cls.username,
            password=cls.password
        )

        cls.leader_id = cls.user
        cls.group_name = 'group_test'

        cls.group = Group.objects.create(
            leader_id = cls.leader_id.id,
            name = cls.group_name
        )

    def test_group_fields(self):
        self.assertIsInstance(self.group.leader_id, int)
        self.assertEqual(self.group.name, 'group_test')

    def test_group_user_relationship(self):      
        users = [
            User.objects.create(
                username=f'user_{i}',
                password='1234',
            ) for i in range(5)
        ]
        
        for user in users:
            self.group.users.add(user)

        self.assertEqual(len(users), self.group.users.count())
        
    def test_join_group_request(self):
        user = User.objects.create(username='test', password=self.password)

        new_request = JoinGroupRequest.objects.create(group=self.group, user=user)

        self.assertIsInstance(new_request.group.id, int)
        self.assertIsInstance(new_request.user.id, int)



