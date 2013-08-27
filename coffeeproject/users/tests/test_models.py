from django.utils import unittest
from django.test import TestCase
from users.models import CoffeeUser
from billing_data.models import Bill

class CoffeeUserBillRelationshipTestCase(TestCase):

    def setUp(self):
        user = CoffeeUser.objects.create(username="bagelman", password="frolick", email="ashy@elbows.com")
        Bill.objects.create(title="bill_1", user=user)
        Bill.objects.create(title="bill_2", user=user)
        Bill.objects.create(title="bill_3", user=user)

    def test_user_has_many_bills(self):
        user = CoffeeUser.objects.get(username="bagelman", password="frolick", email="ashy@elbows.com")
        self.assertEqual(user.get_bills().count(), 3)

    def test_bill_has_unique_user(self):
        bill = Bill.objects.get(title="bill_3")
        self.assertEqual(bill.user, CoffeeUser.objects.get(username="bagelman", password="frolick", email="ashy@elbows.com"))

