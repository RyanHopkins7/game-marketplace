from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

class TestAccounts(TestCase):
    def test_create_user(self):
        user1 = User(username="testuser1", password="testpassword57")
        user1.save()
        user2 = User(username="testuser2", password="testpassword58")
        user2.save()

        self.assertEquals(len(User.objects.all()), 2)

    def test_unique_user(self):
        user1 = User(username="testuser", password="testpassword57")
        user1.save()

        user2 = User(username="testuser", password="testpassword58")
        self.assertRaises(IntegrityError, user2.save)
