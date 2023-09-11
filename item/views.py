from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.
def detail(request, pk):
    item=get_object_or_404(Item, pk=pk)# if item does not exist, return 404 error
    related_items= Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)[:3]# get 3 related items
    return render(request, 'item/detail.html', {'item':item,
                                                'related_items':related_items
                                                })# render the item detail page