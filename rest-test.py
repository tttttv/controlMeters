import requests
import json

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY3ZGM3NjI1LWZkODctNDEzOS1hYTg1LTg0YjQ4ZDJmODQxZSIsInR5cCI6ImtleSJ9.C4920IZCJ4iAZBPdIaHqrl5f0bUIHDEZIJN0AKymCvM'

url = 'http://51.250.78.89:8090/api/devices'
headers = {
    'Authorization': 'Bearer ' + token
}

eui = '8cc30232011a52cf'
url = 'http://51.250.78.89:8090/api/devices/' + eui + '/events'

params = {
    'applicationId': 'f7cf6e15-a9a8-41e8-a485-4435e6f75d4d',
    'limit': 100
}
r = requests.post(url, headers=headers, params=params)
print(r.text)
print(json.dumps(r.json(), indent=4))
