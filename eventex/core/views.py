# coding: utf-8
from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def template_view(request, template_name):
	return render(request, template_name + '.html')