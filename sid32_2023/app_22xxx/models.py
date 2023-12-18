from django.db import models
from django.urls import reverse

# Create your models here.

class Department(models.Model):
    code = models.CharField(max_length=5, null=False, blank=False, unique=True)
    name = models.CharField(max_length=255, null = False, blank=False)

    def __str__(self):
        return str(self.name)
    
class Module(models.Model):
    code = models.CharField(max_length=5, null=False, blank=False, unique=True)
    label = models.CharField(max_length=255, null = False, blank=False)
    total_cm = models.PositiveIntegerField(null=False, default=0)
    total_td = models.PositiveIntegerField(null=False, default=0)
    total_tp = models.PositiveIntegerField(null=False, default=0)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return str(self.code) + ' --- ' + str(self.label)

