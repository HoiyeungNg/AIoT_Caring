# Instructions for deploying and running: 

## For Moto 360:
open developer mode
choose debug with wifi
adb connect the ip like "192.168.43.20" on laptop/ or use the virtual emulator
change network permission in res/xml/network_security_config for laptop local server ip like "192.168.43.156"
change the url in "HeartRateActivity" like "http://192.168.43.156:8000/mycare/heart_rate"
choose the watch and run the "wear" in android studio
"MyThirdAPP" will be installed 
choose "demo heart rate sensor" in the app

## For microbit:
change the base url in rhub.py like 'http://192.168.43.156:8000/'
link one microbit to laptop
change the serial port listening on the laptop
and run rhub.py

## For backend:
Our database is deployed in the cloud, so there's no need to recreate it locally. However, access to the database is restricted to authorized IP addresses. To obtain access, please follow these steps:
1. Use this website http://ip4.me/ to obtain an IP address in the correct format.
2. Send us the address obtained in step one, and we will manually authorize it for access to the database in the cloud.
3. Once access has been authorized, you can begin using the database normally. Note that if the IP address changes, you will need to repeat this process to regain access.

To run backend：
#install
$ pip install drf-yasg2
$ pip install djangorestframework==3.11.2
$ #start backend service
python manage.py runserver

## For front-end:
Just open the .html file in Chrome.

## For Raspberry Pi:
 install
$ pip install numpy joblib shutil matplotlib
$ pip install tflite-runtime
$ pip install tflite_support 
$ pip install opencv-python opencv-contrib-python
 change the base url in ./source/fall_detection/web_service.py like 'http://192.168.43.156:8000/'
 start camera and alert prediction
$ python ./source/fall_detection/tflite_realtime.py
 Jupyter notebooks can be run on a laptop with opencv installed.
 They and are for Section 3 Prototype Description in the report. 
 They are not necessary to deploy the prototype. 
