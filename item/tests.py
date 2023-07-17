from django.test import TestCase
from .models import Item, Category
from django.contrib.auth.models import User
# Create your tests here.
class ItemModelTest(TestCase):
    def test_item_model_exists(self):
        item=  Item.objects.count()
        self.assertEqual(item,0)
    def test_model_has_string_representation(self):
        category=Category.objects.create(name="Test Category")
        user=User.objects.create_user(username="admin", password="admin")
        # print(user.id)
        item= Item.objects.create(name="Test Product",  price=22, category_id=1, created_by_id=1)
        self.assertEqual(str(item),item.name)

class IndexPageTest(TestCase):
    def setUp(self):
        category=Category.objects.create(name="Test Category")
        user=User.objects.create_user(username="admin", password="admin")
        # print(user.id)
        self.item= Item.objects.create(name="Test Product",  price=22, category_id=1, created_by_id=1)
    def test_index_page_returns_correct_index(self):
        response=self.client.get('/')
        # print(response.templates)
        self.assertTemplateUsed(response,"core/index.html")
        self.assertTemplateUsed(response,"core/base.html")
        self.assertEqual(response.status_code,200)
    def test_index_page_has_items(self):
        response= self.client.get("/")  
        self.assertContains(response,self.item.name)