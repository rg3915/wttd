# coding: utf-8
from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def sobre(request):
	return render(request, 'sobre.html')

def contato(request):
	return render(request, 'contato.html')
