# coding: utf-8
from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def contato(request):
	return render(request, 'contato.html')

def sobre(request):
	return render(request, 'sobre.html')

#def template_view(request, template_name):
#	return render(request, template_name + '.html')