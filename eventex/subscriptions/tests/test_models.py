# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
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

	def test_unicode(self):
		self.assertEqual(u'Regis da Silva', unicode(self.obj))

	def test_paid_default_value_is_False(self):
		'By default paid must be False.'
		self.assertEqual(False, self.obj.paid)

class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		# Create a first entry to force the collision.
		Subscription.objects.create(
			name='Regis da Silva',
			cpf='00000000000',
			email='regis.santos.100@gmail.com',
			phone='11-00000000'
		)

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(
			name='Regis da Silva',
			cpf='00000000000',
			email='segundo@gmail.com',
			phone='11-00000000'
		)
		self.assertRaises(IntegrityError, s.save)

	def test_email_can_repeat(self):
		'Email is not unique anymore.'
		s = Subscription.objects.create(
			name='Regis da Silva',
			cpf='00000000011',
			email='regis.santos.100@gmail.com',
			phone='11-00000000'
		)
		self.assertEqual(2, s.pk)