from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from assignment4.views import CardCollection
from assignment4.models import Card


class PostAccountTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='card1', password='johnpwd'
        )

    def tearDown(self):
        User.objects.all().delete()
        Card.objects.all().delete()


    def test_post_account_anonymously(self):
        url = reverse(CardCollection.name)
        data = {
            "title": "Test_Card6Title",
            "description": "Test_Card5",
            "status": "in-process"
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_post_account(self):
        self.client.force_authenticate(user=self.user)

        url = reverse(CardCollection.name)
        data = {
                    "title": "Test_Card6Title",
                    "description": "Test_Card5",
                    "status": "in-process"
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED

        # response = self.client.get(url, format='json')
        # assert response.status_code == status.HTTP_200_OK
        # assert len(response.data) == 1
        # assert response.data[0]['name'] == 'Apple'
    #
    # def test_post_same_account_twice(self):
    #     self.client.force_authenticate(user=self.user)
    #
    #     url = reverse(AccountList.name)
    #     data = {
    #         'name': 'Apple',
    #         'industry': 'High Tech'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     assert response.status_code == status.HTTP_201_CREATED
    #     response = self.client.post(url, data, format='json')
    #     assert response.status_code == status.HTTP_400_BAD_REQUEST
    #
    #     response = self.client.get(url, format='json')
    #     assert response.status_code == status.HTTP_200_OK
    #     assert len(response.data) == 1
    #     assert response.data[0]['name'] == 'Apple'
