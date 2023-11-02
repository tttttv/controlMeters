import requests

d = b'{"deduplicationId":"5c2385a4-8b58-4d50-93da-0eda4ddba14e","time":"2023-10-30T20:13:02.608+00:00","deviceInfo":{"tenantId":"52f14cd4-c6f1-4fbd-8f87-4025e1d49242","tenantName":"ChirpStack","applicationId":"f7cf6e15-a9a8-41e8-a485-4435e6f75d4d","applicationName":"new lora","deviceProfileId":"ba01efc2-cebd-44ba-92ef-51739cc16960","deviceProfileName":"lora water meter","deviceName":"8CC30232011A52CF","devEui":"8cc30232011a52cf","tags":{}},"devAddr":"017d4f1a","adr":true,"dr":4,"fCnt":16,"fPort":10,"confirmed":false,"data":"AgEoBiNrBwAAAAAAAAAAdwEAAAA=","rxInfo":[{"gatewayId":"028166fffe6a29fd","uplinkId":34476,"time":"2023-10-30T20:13:02.608474+00:00","timeSinceGpsEpoch":"1382732000.608s","rssi":-50,"snr":-8.2,"channel":3,"location":{},"context":"L/VZ2g==","metadata":{"region_common_name":"EU868","region_config_id":"eu868"},"crcStatus":"CRC_OK"}],"txInfo":{"frequency":867100000,"modulation":{"lora":{"bandwidth":125000,"spreadingFactor":8,"codeRate":"CR_4_5"}}}}'
params = {
  'event': 'up'
}
url = 'http://51.250.83.110/chirpstack'

r = requests.post(url=url, params=params, data=d)
print(r.status_code)