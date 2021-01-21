from collections import OrderedDict
import time
import config
import requests
import json
#import RPi.GPIO as GPIO
#import dht11

import Adafruit_DHT

# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor = Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio = 17

# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')


# while True:
#   # Get Unix timestamp
#     timestamp = int(time.time())

print('hola')

""" build_json = {
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
 """
