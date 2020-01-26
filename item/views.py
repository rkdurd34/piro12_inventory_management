from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import ItemForm, CustomerForm
from .models import Item, Customer


# Create your views here.
def list_item(request):
    qs = Item.objects.all()
    return render(request, 'item/list_item.html', {
        'item_list': qs,

    })
def detail_item(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'item/detail_item.html', {
        'item': item,
    })
create_item = CreateView.as_view(model=Item, form_class=ItemForm)
register_customer = CreateView.as_view(model=Customer, form_class=CustomerForm)


def detail_customer(request,pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'item/detail_customer.html', {
        'customer': customer,
    })



def list_customer(request):
    pass


def edit_item(request, pk):
    pass


def edit_customer(request, pk):
    pass
