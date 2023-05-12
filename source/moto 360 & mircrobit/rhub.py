import serial
import sys
import os
import time
import requests
import json
import datetime


def upload_temp(temp):
    try:
    
        base_uri = 'http://192.168.43.156:8000/'
        globaltemperature_uri = base_uri + 'mycare/temperature'
        headers = {'content-type': 'application/json'}
        timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        
        gtemp = {
            "temperature" :float(temp),
            "update_time" :timestamp
        }
        print(gtemp)
        req = requests.post(globaltemperature_uri, headers = headers, data = json.dumps(gtemp))
        print(req)
        if req.status_code >= 200 and req.status_code < 300:
                print("Temperature data uploaded successfully.")
        else:
            print("Failed to upload temperature data. Status code: ", req.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred during the HTTP POST request:", e)
    except ValueError as ve:
        print("Error converting temperature to float:", ve)
    except Exception as ex:
        print("An unexpected error occurred:", ex)
			




def sendCommand(command):
    command = command + '\n'
    ser.write(str.encode(command))


def waitResponse():
    response = ser.readline()
    response = response.decode('utf-8').strip()
    return response


try:
    noResponce = False
    print("Listening on COM12... Press CTRL+C to exit")

    ser = serial.Serial(port='COM12', baudrate=115200, timeout=1)

    # Handshaking
    sendCommand('handshake')

    strMicrobitDevices = ''

    while strMicrobitDevices == None or len(strMicrobitDevices) <= 0:

        strMicrobitDevices = waitResponse()

        time.sleep(0.1)

    strMicrobitDevices = strMicrobitDevices.split('=')

    if len(strMicrobitDevices[1]) > 0:

        listMicrobitDevices = strMicrobitDevices[1].split(',')

        if len(listMicrobitDevices) > 0:

            for mb in listMicrobitDevices:

                print('Connected to micro:bit device {}...'.format(mb))

            basetime = time.time()

            while True:

                time.sleep(1)
                #every 10 sec
                if time.time() - basetime > 10:
                    print('Sending command to all micro:bit devices...')
                    commandToTx = 'sensor=temp'
                    sendCommand('cmd:' + commandToTx)
                    print('Finished sending command to all micro:bit devices...')

                    basetime = time.time()

                    
                    if commandToTx.startswith('sensor='):
                        strSensorValues = ''

                        waitbase = time.time()
                        while strSensorValues == None or len(strSensorValues) <= 0:
                            strSensorValues = waitResponse()
                            time.sleep(0.1)
                            if time.time() - waitbase > 8 :
                                noResponce = True
                                break
                        if not noResponce: 
                            listSensorValues = strSensorValues.split(',')
                            for sensorValue in listSensorValues:
                                print(sensorValue)
                                value = sensorValue.split('=')
                                if len(value) > 1:
                                    upload_temp(value[1])

                        noResponce = False

                

except KeyboardInterrupt:
    print("Program terminated!")

finally:
    if ser.is_open:
        ser.close()

    
