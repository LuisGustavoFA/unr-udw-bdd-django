from django.urls import path
from . import views

app_name = 'modeloapp2'

urlpatterns = [
    path('', views.home, name='home'),
]