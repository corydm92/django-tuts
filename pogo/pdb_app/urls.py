from django.contrib import admin
from django.urls import path
from . import views

app_name = "pdb_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>', views.item, name='item')
]