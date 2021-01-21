from collections import OrderedDict
import time
import config
import requests
import json
#import RPi.GPIO as GPIO
import dht11

# while True:
#   # Get Unix timestamp
#     timestamp = int(time.time())
timestamp = 'feliz cumpleaños'
print('hola')

build_json = {
    "iot2tangle": [],
    "device": str(config.device_id),
    "timestamp": str(timestamp)
}
# Set Json headers
headers = {"Content-Type": "application/json"}

# Send Data to Json server
try:
    build_json = json.dumps(build_json)
    r = requests.post(config.endpoint, data=build_json, headers=headers)
    r.raise_for_status()
    print(":: Sending datasets ::")
    print("--------------------------------------------------------")
    print(build_json)

except:

    print("No server listening at " + str(config.endpoint))

    # Interval
    time.sleep(config.relay)
