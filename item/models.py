from django.db import models
from page.utils import uuid_upload_to
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=10,verbose_name="이름")
    tel = models.PositiveIntegerField(verbose_name="전화번호")
    address = models.CharField(max_length=50,verbose_name="주소")

    def get_absolute_url(self):

        return reverse('item:detail_customer', args=[self.pk])
        # return reverse('item:detail_item.html', kwargs = {'pk' : self.pk})

class Item(models.Model):
    title = models.CharField(max_length=20,verbose_name="제품명")
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to,verbose_name="제품 사진")
    content = models.TextField(verbose_name="제품 설명")
    price = models.PositiveIntegerField(verbose_name="가격")
    rest_quantity = models.PositiveIntegerField(verbose_name="남은 수량")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="거래처")

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('item:detail_item', args=[self.pk])
        # return reverse('item:detail_item.html', kwargs = {'pk' : self.pk})


