from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import StoreCreateView
from apps_content.biblioteca.models import Store
import json

#class StoreTests(TestCase):
#    def test_store_status_code(self):
#        url = reverse('create_store')
#        response = self.client.get(url)
#        self.assertEquals(response.status_code, 200)

#    def test_store_url_resolves_store_view(self):
#        view = resolve("/store/list")
#        self.assertEquals(view.__class__, StoreCreateView)
5

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list_store')

    def test_store_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/list-store.html')
