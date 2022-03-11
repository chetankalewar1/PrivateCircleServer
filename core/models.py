from django.db import models

# Create your models here.


class EquityStockWatch(models.Model):
    symbol = models.CharField(max_length=255)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    ltp = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=10, decimal_places=2)
    change_percent = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    turnover = models.DecimalField(max_digits=10, decimal_places=2)
    high_52 = models.DecimalField(max_digits=10, decimal_places=2)
    low_52 = models.DecimalField(max_digits=10, decimal_places=2)
    chang_percent_365 = models.DecimalField(max_digits=10, decimal_places=2)
    chang_percent_30 = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symbol



