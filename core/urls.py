from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-of-use/', views.terms, name='terms'),
]