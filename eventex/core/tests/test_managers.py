# -*- coding: utf-8 -*-
from django.test import TestCase
from eventex.core.models import Contact, Speaker, Talk

class ContactManagerTest(TestCase):
	def setUp(self):
		s = Speaker.objects.create(
			name='Regis da Silva',
			slug='regis-da-silva',
			url='http://regis-wttd.herokuapp.com/'
		)
		s.contact_set.add(Contact(kind='E', value='regis.santos.100@gmail.com'),
			              Contact(kind='P', value='11-1234-5678'),
			              Contact(kind='F', value='11-1234-5670'),)

	def test_emails(self):
		qs = Contact.emails.all()
		expected = ['<Contact: regis.santos.100@gmail.com>']
		self.assertQuerysetEqual(qs, expected)

	def test_phones(self):
		qs = Contact.phones.all()
		expected = ['<Contact: 11-1234-5678>']
		self.assertQuerysetEqual(qs, expected)

	def test_faxes(self):
		qs = Contact.faxes.all()
		expected = ['<Contact: 11-1234-5670>']
		self.assertQuerysetEqual(qs, expected)

class PeriodManagerTest(TestCase):
	def setUp(self):
		Talk.objects.create(title='Morning Talk', start_time='10:00')
		Talk.objects.create(title='Afternoon Talk', start_time='12:00')

	def test_morning(self):
		'Should return only talks before 12:00.'
		self.assertQuerysetEqual(Talk.objects.at_morning(), ['Morning Talk'], lambda t: t.title)

	def test_afternoon(self):
		'Should return only talks after 11:59:59.'
		self.assertQuerysetEqual(Talk.objects.at_afternoon(), ['Afternoon Talk'], lambda t: t.title)

