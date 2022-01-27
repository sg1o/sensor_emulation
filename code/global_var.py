###########################################################
#   ____ _    ____ ___  ____ _    _  _ ____ ____   ____   #
#   | __ |    |  | |__] |__| |    |  | |__| |__/  [__     #
#   |__] |___ |__| |__] |  | |___  \/  |  | |  \  ___]    #
#                                                         #
###########################################################

from ctypes.wintypes import INT
import paho.mqtt.client as paho #type: ignore
import sys
import ssl
from ui import *
import configparser


"""Archivo de configuración"""
parser = configparser.ConfigParser()
parser.read("conf.ini")


object_gui = None
piso = int(parser["Settings"]["piso"])

'''Logging Files'''

temp_log = str(parser["Settings"]["temp_log"])
hum_log = str(parser["Settings"]["hum_log"])
cons_log = str(parser["Settings"]["cons_log"])
presence_log = str(parser["Settings"]["presence_log"])
lum_log = str(parser["Settings"]["lum_log"])

'''Variables for power consumption'''
power_unit = 'kw'

'''Variables for temperature'''
actual_temp = 20
temp_unit = ' C'

'''Variable for humidity'''
actual_hum = 50
hum_unit = ' %'

'''Variable for luminosity'''
max_lum = 3000
lum_unit = ' lm'

'''Intervals'''
temp_interval = None
hum_interval = None

'''MQTT paho Global Variables'''
broker = str(parser["Settings"]["IP"])
port  = int(parser["Settings"]["PORT"])


'''Topic Config'''
apikey = str(parser["Settings"]["apikey"])

temp_object_id = str(parser["Settings"]["temp_object_id"])
temp_device_id = str(parser["Settings"]["temp_device_id"])


hum_object_id = str(parser["Settings"]["hum_object_id"])
hum_device_id = str(parser["Settings"]["hum_device_id"])

power_object_id = str(parser["Settings"]["power_object_id"])
power_device_id = str(parser["Settings"]["power_device_id"])

presen_object_id = str(parser["Settings"]["presen_object_id"])
presen_device_id = str(parser["Settings"]["presen_device_id"])

luz_object_id = str(parser["Settings"]["luz_object_id"])
luz_device_id = str(parser["Settings"]["luz_device_id"])


'''MQTT CONNECTION'''

def on_publish(client, data, ret):
    print("[+] Packet sended")

try:
    mqtt_client = paho.Client("control_panel")
except:
    print("[!] Problem creating MQTT client...")
    sys.exit()

try:
    mqtt_client.on_publish = on_publish
except:
    print("[!] Problem creating MQTT client...")
    sys.exit()

try:

    ca = str(parser["CERTS"]["ca"])
    cert = str(parser["CERTS"]["client"])
    key = str(parser["CERTS"]["key"])
    mqtt_client.tls_set(ca_certs=ca, certfile=cert,
                                keyfile=key, cert_reqs=ssl.CERT_REQUIRED, ciphers=None)
    
    mqtt_client.tls_insecure_set(True)
    mqtt_client.connect(broker, port, keepalive=9999)
except:
    print("[!] Problem in client connect...")
    sys.exit()