from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django import forms

from .models import Item


# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items':items})


class ItemCreate(CreateView):
    model = Item
    fields = ['description']
    success_url = '/'

def item_delete(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('/')