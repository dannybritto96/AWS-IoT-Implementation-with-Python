import paho.mqtt.client as paho
import os
import socket
import ssl
import json

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    client.subscribe("quality")

def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    payload = msg.payload
    payload = json.loads(payload)
    print(payload)

def on_log(client, userdata, level, msg):
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

mqttc.loop_forever()
