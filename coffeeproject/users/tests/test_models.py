from django.utils import unittest
from django.test import TestCase
from users.models import TestModel, RelatedTestModel

class UserBillRelationshipTestCase(TestCase):

	def setUp(self):
		user = TestModel.objects.create(title="user")
		RelatedTestModel.objects.create(title="bill_1", test_model=user)
		RelatedTestModel.objects.create(title="bill_2", test_model=user)
		RelatedTestModel.objects.create(title="bill_3", test_model=user)

	def test_user_has_many_bills(self):
		user = TestModel.objects.get(title="user")
		self.assertEqual(user.get_bills().count(), 3)

	def test_bill_has_user(self):
		bill = RelatedTestModel.objects.get(title="bill_2")
		self.assertEqual(bill.test_model, TestModel.objects.get(title="user"))


