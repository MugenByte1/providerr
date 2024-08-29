from django.db import models
from provider.models import customer,seller
from int.models import inter

class Order(models.Model):
        customerr = models.ForeignKey(customer, on_delete=models.CASCADE, blank=True, null=True)
        sellererr = models.ForeignKey(seller, on_delete=models.CASCADE, blank=True, null=True)

        transaction_status = models.BooleanField(blank=True, null=True)
        account = models.IntegerField(default= 100)

add

