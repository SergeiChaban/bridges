from django.test import TestCase
from Service.models import  Service



@classmethod
	def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Service.objects.create( name='Service')

    def test_first_name_label(self):
        service=Service.objects.get(id=1)
        field_label = service._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')


    def test_name_max_length(self):
        service=Service.objects.get(id=1)
        max_length = service._meta.get_field('name').max_length
        self.assertEquals(max_length,128)
