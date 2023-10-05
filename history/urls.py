from django.urls import path
from . import views

urlpatterns = [
    path('<str:gender>/',views.history, name='history'),
]