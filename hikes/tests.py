from django.test import TestCase
from .models import Hike
from django.contrib.auth import get_user_model

# Create your tests here.
class HikeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="testuser1", password="pass")
        testuser1.save()

        test_hike = Hike.objects.create(name="Lake 22", owner=testuser1, description="Beautiful hike with a lake")
        test_hike.save()

    def test_hikes_model(self):
        hike = Hike.objects.get(id=1)
        actual_owner = str(hike.owner)
        actual_name = str(hike.name)
        actual_description = str(hike.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Lake 22")
        self.assertEqual(actual_description, "Beautiful hike with a lake")