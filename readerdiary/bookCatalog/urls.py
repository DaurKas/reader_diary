from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='catalog-home'),
    path('about/', views.about, name='catalog-about')
]