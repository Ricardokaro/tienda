from rest_framework.test import APITestCase, APIClient
from django.test import Client, TestCase

from tienda.users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse


class TestUrls(APITestCase):
    def setUp(self):
        self.username = 'ricardo'
        self.email = 'ricardo@gmail.com'
        self.password = 'super1'
        self.user = User.objects.create_superuser(self.username, self.email, self.password)
        # self.user = User.objects.create_user()
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_url_is_resolved(self):
        response = self.client.post(
            reverse('categories:category-list'),
            data={
                "name": "Hamburger"
            }
        )
        self.assertEqual(response.status_code, 201)
        pk = response.data['id']
        name = response.data['name']

        response = self.client.get(reverse('categories:category-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], name)
        self.assertEqual(response.data[0]['id'],pk)


    def test_update_category_by_super_user(self):
        pass
