from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

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

edit_item = UpdateView.as_view(model = Item, form_class=ItemForm)
edit_customer = UpdateView.as_view(model = Customer, form_class=CustomerForm)


def list_customer(request):
    qs = Customer.objects.all()
    return render(request, 'item/list_customer.html', {
        'customer_list': qs,

    })

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "GET":
        return redirect('detail_customer', pk=customer.pk)
    elif request.method == 'POST':
        customer.delete()
        return redirect('list_customer')

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == "GET":
        return redirect('detail_item', pk=item.pk)
    elif request.method == 'POST':
        item.delete()
        return redirect("list_item")


