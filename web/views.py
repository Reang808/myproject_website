
from django.shortcuts import render

def index(request):
	return render(request, 'web/index.html')

def about(request):
	return render(request, 'web/about.html')

def faq(request):
	return render(request, 'web/faq.html')

def privacy(request):
	return render(request, 'web/privacy.html')