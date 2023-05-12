# Instructions for deploying and running: 

## For Moto 360:
Open developer mode. <br/>
Choose debug with wifi. <br/>
adb connect the ip like "192.168.43.20" on laptop/ or use the virtual emulator. <br/>
Change network permission in res/xml/network_security_config for laptop local server ip like "192.168.43.156". <br/>
Change the url in "HeartRateActivity" like "http://192.168.43.156:8000/mycare/heart_rate". <br/>
Choose the watch and run the "wear" in android studio. <br/>
"MyThirdAPP" will be installed. <br/>
Choose "demo heart rate sensor" in the app. <br/>

## For microbit:
Change the base url in rhub.py like 'http://192.168.43.156:8000/' <br/>
Link one microbit to laptop. <br/>
Change the serial port listening on the laptop. <br/>
and run rhub.py <br/>

## For backend:
Our database is deployed in the cloud, so there's no need to recreate it locally. However, access to the database is restricted to authorized IP addresses. To obtain access, please follow these steps:<br/>
1. Use this website http://ip4.me/ to obtain an IP address in the correct format.<br/>
2. Send us the address obtained in step one, and we will manually authorize it for access to the database in the cloud.<br/>
3. Once access has been authorized, you can begin using the database normally. Note that if the IP address changes, you will need to repeat this process to regain access.<br/>

To run backend：
#install <br/>
$ pip install drf-yasg2 <br/>
$ pip install djangorestframework==3.11.2 <br/>
$ #start backend service <br/>
python manage.py runserver <br/>

## For front-end:
Just open the .html file in Chrome. <br/>

## For Raspberry Pi:
 install <br/>
$ pip install numpy joblib shutil matplotlib <br/>
$ pip install tflite-runtime <br/>
$ pip install tflite_support <br/>
$ pip install opencv-python opencv-contrib-python <br/>
 Change the base url in ./source/fall_detection/web_service.py like 'http://192.168.43.156:8000/' <br/>
 Start camera and alert prediction <br/>
$ python ./source/fall_detection/tflite_realtime.py <br/>
 Jupyter notebooks can be run on a laptop with opencv installed. <br/>
 They and are for Section 3 Prototype Description in the report. <br/>
 They are not necessary to deploy the prototype. <br/>
