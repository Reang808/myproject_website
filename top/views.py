from django.shortcuts import render

def index(request):
    return render(request, 'top/index.html')

def contact(request):
    return render(request, 'top/contact.html')

def services(request):
    return render(request, 'top/services.html')

def price(request):
    return render(request, 'top/price.html')

def features(request):
    return render(request, 'top/features.html')