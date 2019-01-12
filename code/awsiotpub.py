import paho.mqtt.client as paho
import os
import socket
import ssl
import json
from time import sleep

connflag = False

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_log(client, userdata, level, buf):
    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_log = on_log

awshost = # END POINT URL
awsport = 8883
clientId = "TestThing1"
thingName = "TestThing1"
caPath = "aws-iot-rootCA.crt"
certPath = "cert.pem"
keyPath = "privkey.pem"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

while 1==1:
    sleep(2)
    if connflag == True:
        data = {
            "data": "Hello, World!"
        }
        mqttc.publish("quality", json.dumps(data), qos=1)
        print("msg sent: at {timestamp}".format(timestamp=timestamp) )
    else:
        print("waiting for connection...")
