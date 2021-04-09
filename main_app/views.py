from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def delete(request, item_id):
    Item.objects.get(id=item_id).delete()
    return redirect('/')

class Add(CreateView):
    model = Item
    fields = '__all__'