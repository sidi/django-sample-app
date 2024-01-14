from django.db import models

# Create your models here.

class Currency(models.Model):
    """Class representing a currency"""
    code = models.CharField(max_length=5, unique=True)
    label = models.CharField(max_length=255)

    class Meta:
        """Meta class"""
        ordering = ['-code']

    def __str__(self):
        return str(self.code) + ' --- ' + str(self.label)
    
class Rate(models.Model):
    """Class representing a currency rate converstion to MRU on a given date"""
    unit = models.IntegerField()
    sell = models.FloatField()
    buy = models.FloatField()
    date = models.DateField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    class Meta:
        """Meta class"""
        ordering = ['-id']

    def __str__(self):
        return str(self.date) + ' --- ' + str(self.currency)