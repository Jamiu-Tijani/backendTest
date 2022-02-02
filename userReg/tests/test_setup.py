from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
import os 
from backendTest.settings import BASE_DIR



class TestSetUp(APITestCase):

    def setUp(self):
        self.userReg_url= reverse("User Reg")
        self.fake = Faker()
        self.location = "lagos"

        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email(),
        }
        self.imageUrl = os.path.join(BASE_DIR, "userReg/tests/icon.jpg")
        

        return super().setUp()

    def tearDown(self):
        return super().tearDown()