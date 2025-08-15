from django.urls import path
from . import views

urlpatterns = [
# reservation/urls.py
path('', views.reservation, name='reservation_from')
]