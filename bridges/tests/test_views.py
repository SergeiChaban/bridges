from django.test import TestCase, Client
from django.urls import reverse
from servicesapp.models import Service
import json


# def setUp(self):
#     self.client = Client()
#     self.list_url = reverse('list')


class TestView(TestCase):

    def test_services_list_GET(self):
        client = Client()

        response = client.get(reverse('servicesapp:services_list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'servicesapp/services_list.html')
