from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ERP_CORE.models import WaterMeter, MeterData
from chirpstack_api import integration
from google.protobuf.json_format import Parse

def index_view(request):
    meters = WaterMeter.objects.all()
    meters_data = MeterData.objects.all()

    params = {
        'meters': meters,
        'meters_data': meters_data,
    }
    return render(request, 'index.html', params)


def chirpstack_callback_view(request):
    print(request.POST)
    print(request.GET)
    print(request.body)
    return HttpResponse(status=200)