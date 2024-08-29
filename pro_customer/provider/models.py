from django.db import models

class seller(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'costumer_name', help_text = 'costumer name should be less than 50 characters', blank = True, null = True)
    number = models.CharField(max_length=12, verbose_name= 'phone number', blank = True, null = True)
    acc_status = models.BooleanField(blank = True, null = True)



    def __str__(self) -> str:
        return self.name


class customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='costumer_name', help_text='costumer name should be less than 50 characters', blank=True, null=True)
    number = models.CharField(max_length=12, verbose_name='phone number', blank=True, null=True)
    acc_balance = models.IntegerField(default=100, verbose_name='account balance')


    def __str__(self) -> str:
        return self.name



