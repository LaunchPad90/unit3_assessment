from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.ItemCreate.as_view(), name='item_create'),
    path('item_delete/<int:item_id>/', views.item_delete, name='item_delete'),
]