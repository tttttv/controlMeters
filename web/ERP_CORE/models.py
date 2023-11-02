from django.db import models
import datetime
# Create your models here.

class WaterMeter(models.Model):
    eui = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, default='Без имени')

class MeterData(models.Model):
    meter = models.ForeignKey(WaterMeter, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    dt = models.DateTimeField(default=datetime.datetime.now)