from django.contrib import admin

# Register your models here.
from ERP_CORE.models import WaterMeter, MeterData

admin.site.register(WaterMeter)
admin.site.register(MeterData)