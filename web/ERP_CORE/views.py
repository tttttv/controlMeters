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
    params = {
        'meters': [

        ],
    }
    for meter in meters:
        last_data = MeterData.objects.filter(meter=meter).order_by('-dt').first()

        params['meters'].append({
            'id': meter.id,
            'name': meter.name,
            'eui': meter.eui,
            'last_value': last_data.value if last_data else None,
            'last_dt': last_data.dt.strftime('%d.%m.%Y %H:%M:%S') if last_data else None,
        })

    return render(request, 'index.html', params)

def meter_profile_view(request, pk):
    params = {

    }
    return render(request, 'meter_profile.html', params)

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
        meter_value = meter_value[10:18]
        #meter_value = meter_value[2:10]
        print(meter_value, 'raw')
        meter_value = hex_to_little_endian(meter_value)
        print(meter_value, 'little')
        meter_value = int(meter_value, 16)
        print(meter_value, 'result')

        wm = WaterMeter.objects.get(eui=eui)
        md = MeterData(meter=wm, value=meter_value / 1000, dt=dt)
        md.save()

    elif request.GET['event'] == 'join':
        print('join')


    return HttpResponse(status=200)