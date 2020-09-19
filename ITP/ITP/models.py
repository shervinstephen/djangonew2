from django.db import models

class ChargeInsert(models.Model):

    #id=models.IntegerField
    servicename=models.CharField(max_length=100)
    charge=models.FloatField(max_length=100)
    category=models.CharField(max_length=100)
    class Meta:
        db_table="pricelisttable"