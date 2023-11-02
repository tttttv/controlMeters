from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from ERP_CORE.models import WaterMeter, MeterData
from chirpstack_api import integration
from google.protobuf.json_format import Parse

import base64
import datetime

def hex_to_little_endian(hex_string):
    little_endian_hex = bytearray.fromhex(hex_string)[::-1]
    return ''.join(f"{n:02X}" for n in little_endian_hex)

def index_view(request):
    meters = WaterMeter.objects.all()
    meters_data = MeterData.objects.all()

    params = {
        'meters': meters,
        'meters_data': meters_data,
    }
    return render(request, 'index.html', params)

def unmarshal(body, pl):
    if False:
        return Parse(body, pl)

    pl.ParseFromString(body)
    return pl

@csrf_exempt
def chirpstack_callback_view(request):
    print(request.POST)
    print(request.GET)
    print(request.body)



    body = request.body.decode()
    data = json.loads(body)
    print(data)
    if request.GET['event'] == 'up':
        print('data')
        dt = data['time']
        dt = datetime.datetime.fromisoformat(dt)

        eui = data['deviceInfo']['devEui']

        meter_value = data['data']
        print(meter_value, 'base64')
        meter_value = base64.b64decode(meter_value).hex()
        print(meter_value, 'hex')
        #meter_value = meter_value[10:18]
        meter_value = meter_value[2:10]
        print(meter_value, 'raw')
        meter_value = hex_to_little_endian(meter_value)
        print(meter_value, 'little')
        meter_value = int(meter_value, 16)
        print(meter_value, 'result')

        wm = WaterMeter.objects.get(uid=eui)
        md = MeterData(meter=wm, value=meter_value, dt=dt)
        md.save()

    elif request.GET['event'] == 'join':
        print('join')


    return HttpResponse(status=200)