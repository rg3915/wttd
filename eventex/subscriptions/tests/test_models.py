# coding: utf-8
from django.test import TestCase
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Regis da Silva',
			cpf='00000000000',
			email='regis.santos.100@gmail.com',
			phone='11-00000000'
		)

	def test_create(self):
		'Subscription must have name, cpf, email, phone'
		self.obj.save()
		self.assertEqual(1, self.obj.pk)

	def test_has_created_at(self):
		'Subscription must have automatic created_at.'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)