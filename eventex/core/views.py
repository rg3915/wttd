# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker

def home(request):
	return render(request, 'index.html')

def contato(request):
	return render(request, 'contato.html')

def sobre(request):
	return render(request, 'sobre.html')

def speaker_detail(request, slug):
	speaker = get_object_or_404(Speaker, slug=slug)
	context = {'speaker': speaker}
	return render(request, 'core/speaker_detail.html', context)

def talk_list(request):
	return render(request, 'core/talk_list.html')

#def template_view(request, template_name):
#	return render(request, template_name + '.html')