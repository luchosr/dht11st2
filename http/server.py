#from sense_hat import SenseHat
from collections import OrderedDict
""" sense=SenseHat()
sense.clear() """
import time
import config
import requests
import json
import RPi.GPIO as GPIO
import dht11

""" GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=14) """

while True:
  # Get Unix timestamp
    timestamp = int(time.time())

#result = instance.read()

""" if result.is_valid():
    build_json['iot2tangle'].append({
        "sensor": "DHT11",
        "data": [{
            "Temp":"temperatura"
            # str("Temperature: %-3.1f C" % result.temperature)
        },{
            "Humidity": "humedad"
            #str("Humidity: %-3.1f %%" % result.humidity)
        }]
    })    
 """


    # Json open
build_json = {
    "iot2tangle": [],
    "device":str(config.device_id),
    "timestamp":str(timestamp)
}
    # Set Json headers
headers = {"Content-Type": "application/json"}

# Send Data to Json server
try:
    build_json = json.dumps(build_json)
    r = requests.post(config.endpoint, data=build_json, headers=headers)
    r.raise_for_status()
    print (":: Sending datasets ::")
    print("--------------------------------------------------------")
    print(build_json)

except :

    print ("No server listening at " + str(config.endpoint))

    # Interval
    time.sleep(config.relay)
