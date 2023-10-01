from django.urls import path
from . import views

urlpatterns = [
    path('', views.boy, name = 'history'),
    path('boy/', views.boy, name = 'boy'),
    path('girl/', views.girl, name = 'girl')
]