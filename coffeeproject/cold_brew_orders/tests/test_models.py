from django.utils import unittest
from django.test import TestCase
from users.models import CoffeeUser
from billing_data.models import Bill
from shipping_data.models import ShippingAddress
from cold_brew_orders.models import ColdBrewOrder

class ColdBrewOrderFunctionality(TestCase):

    def setUp(self):
        user = CoffeeUser.objects.create(
            username="paintball", 
            password="screwball", 
            email="cheeseball@bacon.com",
            )
        shipping_data_object = ShippingAddress.objects.create()
        ColdBrewOrder.objects.create(
            info='miralvalle;32oz Growler;5;14.00,villa sarchi;16oz Growler;5;12.00',
            notes='Please leave coffee in the mailbox',
            user=user,
            shipping_address=shipping_data_object,
            )
        
    def test_unicode_function(self):
        self.assertEqual(type(u'a'), type(ColdBrewOrder.objects.all()[0].__unicode__()))

    def test_order_has_unique_user(self):
        user = CoffeeUser.objects.get(
            username="paintball", 
            password="screwball", 
            email="cheeseball@bacon.com",
            )
        coldbreworder = ColdBrewOrder.objects.all()[0]
        self.assertEquals(coldbreworder.user, user)

    def test_order_has_unique_shipping_address(self):
        coldbreworder = ColdBrewOrder.objects.all()[0]
        shipping_address = ShippingAddress.objects.all()[0]
        self.assertEquals(coldbreworder.shipping_address, shipping_address)

    def test_order_function_parses_info_correctly(self):
        coldbreworder = ColdBrewOrder.objects.all()[0]
        self.assertEquals(coldbreworder.parse_order_info(), [['miralvalle', '32oz Growler', '5', '14.00'], ['villa sarchi', '16oz Growler', '5', '12.00']])