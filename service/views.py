from django.shortcuts import render
from .models import Service

def service(request):
    services = Service.objects.all()
    return render(request, 'service/service.html', {'services': services})

def reserve(request):
    return render(request, 'service/reserve.html')

def linebizconnect(request):
    return render(request, 'service/linebizconnect.html')

def webboosters(request):
    return render(request, 'service/webboosters.html')