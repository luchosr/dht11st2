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

while True:
  # Get Unix timestamp
    timestamp = int(time.time())



    # Json open
    build_json = {
        "iot2tangle": [],
        "device":str(config.device_id),
        "timestamp":str(timestamp)
    }
""" 
    # If Enviromental
    if config.enviromental:
        build_json['iot2tangle'].append({
            "sensor": "Enviromental",
            "data": [{
                "Pressure": str(press),
                "Temp": str(temp)
            },{
                "Humidity": str(humidity)
            }]
        })
 """

"""     if config.dht11:
        build_json['iot2tangle'].append({
            "sensor": "dht11",
            "data": [{
                "Pressure": str(press),
                "Temp": str(temp)
            },{
                "Humidity": str(humidity)
            }]
        }) """

""" 
    #If Accelerometer
    if config.accelerometer:
        build_json['iot2tangle'].append({
            "sensor": "Accel",
            "data": [{
                "x": str(x_accelerometer),
                "y": str(y_accelerometer),
                "z": str(z_accelerometer)
            }]
        })

    # If Gyroscope
    if config.gyroscope:
        build_json['iot2tangle'].append({
            "sensor": "Gyroscope",
            "data": [{
                "x": str(x_gyroscope),
                "y": str(y_gyroscope),
                "z": str(z_gyroscope)
            }]
        })

    # If Magonetometer
    if config.magnetometer:
        build_json['iot2tangle'].append({
            "sensor": "Magnetometer",
            "data": [{
                "x": str(x_compass),
                "y": str(y_compass),
                "z": str(z_compass)
            }]
        }) """

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
