import requests

d =  b'{"deduplicationId":"f068ce00-6e59-49cc-b979-13f48dceafa7","time":"2023-11-23T00:06:01.156927957+00:00","deviceInfo":{"tenantId":"52f14cd4-c6f1-4fbd-8f87-4025e1d49242","tenantName":"ChirpStack","applicationId":"f7cf6e15-a9a8-41e8-a485-4435e6f75d4d","applicationName":"new lora","deviceProfileId":"ba01efc2-cebd-44ba-92ef-51739cc16960","deviceProfileName":"lora water meter","deviceName":"8CC30232011A52CF","devEui":"8cc30232011a52cf","tags":{}},"devAddr":"01dbce85","adr":true,"dr":0,"fCnt":0,"fPort":10,"confirmed":false,"data":"AgEoBiPdDgAAAAAAAAAAdwEAAAA=","rxInfo":[{"gatewayId":"028166fffe6a29fd","uplinkId":16174,"rssi":-46,"snr":-17.5,"channel":4,"location":{"latitude":55.52444,"longitude":34.00512,"altitude":3473.0},"context":"7w3rlw==","metadata":{"region_common_name":"EU868","region_config_id":"eu868"},"crcStatus":"CRC_OK"}],"txInfo":{"frequency":867300000,"modulation":{"lora":{"bandwidth":125000,"spreadingFactor":12,"codeRate":"CR_4_5"}}}}'
params = {
  'event': 'up'
}
url = 'http://51.250.83.110/chirpstack'
#url = 'http://127.0.0.1:8000/chirpstack'

r = requests.post(url=url, params=params, data=d)
print(r.status_code)