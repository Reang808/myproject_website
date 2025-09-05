
from django.shortcuts import render

def index(request):
	return render(request, 'web/index.html')

def about(request):
	return render(request, 'web/about.html')

def price(request):
	return render(request, 'web/price.html')