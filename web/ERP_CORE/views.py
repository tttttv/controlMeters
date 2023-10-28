from django.shortcuts import render

# Create your views here.
from web.ERP_CORE.models import WaterMeter, MeterData


def index_view(request):
    meters = WaterMeter.objects.all()
    meters_data = MeterData.objects.all()

    params = {
        'meters': meters,
        'meters_data': meters_data,
    }
    return render(request, 'index.html', params)