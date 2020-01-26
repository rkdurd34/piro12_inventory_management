from django import forms
from .models import Item,Customer
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"