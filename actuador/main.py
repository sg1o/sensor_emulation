from http.client import OK
import paho.mqtt.client as mqtt
import ssl
import signal
import sys
import os

def signal_handler(sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

QOS = 2
HOST = "192.168.0.22"
PORT = 8883
topic = "actuador" # /testingSCO/
KEEPALIVE = 9999
persiana = False
luz = False

ca = "/home/sergio/Documents/master/SCO/sensor_emulation/actuador/ca.crt"
cert = "/home/sergio/Documents/master/SCO/sensor_emulation/actuador/client2.crt"
key = "/home/sergio/Documents/master/SCO/sensor_emulation/actuador/client2.key"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))
    client.subscribe("actuador")

def offPersiana():
    #os.system("clear")
    print("[!]Cerrando persiana...\n\n")
    file = open("asciiArt/persianaCerrada", 'r')
    text = file.read()
    print(text, end='\n\n')

def onPersiana():
    #os.system("clear")
    print("[!]Abriendo persiana...\n\n")
    file = open("asciiArt/persianaAbierta", 'r')
    text = file.read()
    print(text, end='\n\n')

def lightOn():
    #os.system("clear")
    print("[!]Encendiendo luz...\n\n")
    file = open("asciiArt/luzEncendida", 'r')
    text = file.read()
    print(text, end='\n\n')

def lightOff():
    #os.system("clear")
    print("[!]Apagando luz...\n\n")
    file = open("asciiArt/luzApagada", 'r')
    text = file.read()
    print(text, end='\n\n')

def ok(msg):
    msg = id@command | command OK
    msg--> mqtt pub con topic

def on_message(mclient, user, msg):
    global luz, persiana
    entrada = msg.payload.decode('utf-8')
    ok(msg)
    if  "lightOff" in entrada and luz:
        lightOff()
        luz = False

    if "lightOn" in entrada and not luz:
        lightOn()
        luz = True

    if "persianaOpen" in entrada and not persiana:
        onPersiana()
        persiana = True

    if "persianaClose" in entrada and persiana:
        offPersiana()
        persiana = False


def main():

    global object_gui
    print("[+]Running...")

    try:
        client = mqtt.Client()

        client.on_connect = on_connect
        client.on_message = on_message

        client.tls_set(ca_certs=ca, certfile=cert,
                                    keyfile=key, cert_reqs=ssl.CERT_REQUIRED, ciphers=None)
        client.tls_insecure_set(True)

        
        client.subscribe((topic, QOS))
        client.connect(HOST, PORT, keepalive=KEEPALIVE)

    except:
        print("[!]Error in mqtt")
    
    client.loop_forever()


if __name__ == "__main__":
    main()