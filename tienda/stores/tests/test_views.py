from rest_framework.test import APITestCase, APIClient
from tienda.users.models import User
from tienda.stores.models import Store
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

class TestViews(APITestCase):
    def setUp(self):
        self.username = 'ricardo'
        self.email = 'ricardo@gmail.com'
        self.password = 'super1'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def save_store(self, data):
        return self.client.post(
            reverse('stores:store-list'),
            data = data
        )

    def test_save_store(self):
        response = self.save_store({'name':'Olimpica','address':'Calle 23 # 3-05'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Store.objects.count(), 1)
        self.assertEqual(Store.objects.get().name, 'Olimpica')

    def test_get_store_admin(self):
        self.save_store({'name': 'Olimpica', 'address': 'Calle 23 # 3-05'})
        self.user = User.objects.get(id=self.user.id)

        """Verifica que su estado haya cambiado a administrador"""
        self.assertTrue(self.user.is_admin)

        response = self.client.get(
            reverse('stores:store-list')
        )
        self.assertEqual(response.status_code, 200)

        owner = User.objects.get(id = response.data[0]['owner']['id'])
        self.assertEqual(owner, self.user)


