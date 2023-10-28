from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ERP_CORE.models import WaterMeter, MeterData


def index_view(request):
    meters = WaterMeter.objects.all()
    meters_data = MeterData.objects.all()

    params = {
        'meters': meters,
        'meters_data': meters_data,
    }
    return render(request, 'index.html', params)


def callback_data(request):

    return HttpResponse(status=200)