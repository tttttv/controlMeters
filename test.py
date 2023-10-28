import os
import sys

import grpc
from chirpstack_api import api

# Configuration.

# This must point to the API interface.
server = "51.250.78.89:8080"

# The DevEUI for which you want to enqueue the downlink.
dev_eui = "8a22233201314d19"

# The API token (retrieved using the web-interface).
api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY3ZGM3NjI1LWZkODctNDEzOS1hYTg1LTg0YjQ4ZDJmODQxZSIsInR5cCI6ImtleSJ9.C4920IZCJ4iAZBPdIaHqrl5f0bUIHDEZIJN0AKymCvM"

if __name__ == "__main__":
  # Connect without using TLS.
  channel = grpc.insecure_channel(server)

  # Device-queue API client.
  #client = api.DeviceServiceStub(channel)
  client = api.InternalServiceStub(channel)

  # Define the API key meta-data.
  auth_token = [("authorization", "Bearer %s" % api_token)]

  # Construct request.

  req = api.StreamDeviceFrames()

  #req = api.StreamDeviceFramesRequest()
  #req.queue_item.confirmed = False
  #req.queue_item.data = bytes([0x01, 0x02, 0x03])
  #req.queue_item.dev_eui = dev_eui
  #req.queue_item.f_port = 10

  resp = client.Enqueue(req, metadata=auth_token)

  # Print the downlink id
  print(resp)
