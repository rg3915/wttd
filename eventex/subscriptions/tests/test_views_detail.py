# -*- coding: utf-8 -*-
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(
			name='Regis da Silva',
			cpf='00000000000',
			email='regis.santos.100@gmail.com',
			phone='11-00000000'
		)
		self.resp = self.client.get('/inscricao/%d/' % s.pk)

	def test_get(self):
		'GET /inscricao/1/ should return status 200.'
		self.assertEqual(200, self.resp.status_code)