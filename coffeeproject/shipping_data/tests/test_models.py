from django.utils import unittest
from django.test import TestCase
from shipping_data.models import ShippingAddress

class ShippingDataTestCase(TestCase):

    def setUp(self):
        shipping_address_object = ShippingAddress()
        shipping_address_object.save()

    def test_unicode_function(self):
        shipping_address_object = ShippingAddress.objects.all()[0]
        self.assertEqual(type(u'a'), type(shipping_address_object.__unicode__()))