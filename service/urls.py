from django.urls import path
from . import views



urlpatterns = [
    path('', views.service, name='service'),
    path('reseline/', views.reseline, name='reseline'),
    path('linebizconnect/', views.linebizconnect, name='linebizconnect'),
    path('webboosters/', views.webboosters, name='webboosters'),
]