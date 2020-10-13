from rest_framework.test import APITestCase, APIClient
from tienda.users.models import User
from tienda.categories.models import Category
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

    def test_save_category(self):
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
        category = Category.objects.create(name='Tecnologia')
        data = {'name':'Deportes'}
        response = self.client.patch('/categories/'+str(category.id)+'/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], category.id)
