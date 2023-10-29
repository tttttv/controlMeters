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

def unmarshal(self, body, pl):
    if self.json:
        return Parse(body, pl)

    pl.ParseFromString(body)
    return pl

def chirpstack_callback_view(request):
    print(request.POST)
    print(request.GET)
    print(request.body)

    
    body = request.body
    try:
        up = unmarshal(body, integration.UplinkEvent())
        print("Uplink received from: %s with payload: %s" % (up.device_info.dev_eui, up.data.hex()))
    except:
        join = unmarshal(body, integration.JoinEvent())
        print("Device: %s joined with DevAddr: %s" % (join.device_info.dev_eui, join.dev_addr))

    return HttpResponse(status=200)