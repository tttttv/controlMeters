from django.db import models
import datetime
# Create your models here.

class WaterMeter(models.Model):
    uid = models.CharField(max_length=100, unique=True)

class MeterData(models.Model):
    meter = models.ForeignKey(WaterMeter, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    dt = models.DateTimeField(default=datetime.datetime.now)