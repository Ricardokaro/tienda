from rest_framework.test import APITestCase, APIClient
from tienda.users.models import User
from tienda.stores.models import Store
from rest_framework.authtoken.models import Token
from django.urls import resolve, reverse
from tienda.stores.models import Store


class TestViews(APITestCase):
    def setUp(self):
        self.username = 'ricardo'
        self.email = 'ricardo@gmail.com'
        self.password = 'super1'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.store = Store.objects.create(name='Olimpica', address='Calle 23 # 3-05', user=self.user, owner=self.user)

    def test_store_list(self):
        assert reverse("stores:store-list") == "/stores/"
        assert resolve("/stores/").view_name == "stores:store-list"

    def test_user_detail(self):
        assert (
            reverse("stores:store-detail", kwargs={"pk": self.store.id})
            == f"/stores/{self.store.id}/"
        )
        assert resolve(f"/stores/{self.store.id}/").view_name == "stores:store-detail"
