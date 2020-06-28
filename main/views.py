from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response,id):
    ls = ToDoList.objects.get(id=id)
    items = ls.item_set.get(id=id)
    return HttpResponse("<h1>%s<h1/><br></br><p>%s</p>" %(ls.name,items.text))




    