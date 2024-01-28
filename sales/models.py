from django.db import models
import uuid

# Create your models here.

class Sale(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=255)
    quantity_sold = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)