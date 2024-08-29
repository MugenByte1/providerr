from django.db import models
from provider.models import seller

class inter(models.Model):
    sellerr = models.ForeignKey(seller, on_delete = models.CASCADE)

    trafic_based = models.IntegerField(default = 100)
    price = models.IntegerField(default = 100)

