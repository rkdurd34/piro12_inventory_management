from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "item"
urlpatterns = [

    path('', views.list_item, name="list_item"),
    path('detail/item/<int:pk>', views.detail_item, name="detail_item"),
    path('create/',views.create_item, name = 'create_item'),
    path('register/',views.register_customer, name="register_customer"),
    path('detail/customer/<int:pk>',views.detail_customer, name='detail_customer'),
    path('list/customer',views.list_customer, name='list_customer'),
    path('edit/item/<int:pk>', views.edit_item,name="edit_item"),
    path('edit/customer/<int:pk>', views.edit_customer,name="edit_customer"),
    path('delete/customer/<int:pk>',views.delete_customer, name='delete_customer'),
    path('delete/item/<int:pk>',views.delete_item, name='delete_item')
]
