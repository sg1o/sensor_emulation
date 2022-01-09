import random
import time
import threading
import signal
from global_var import * #type: ignore


def get_temp():
    '''
     In this case, the function returns a random temperature value,
     but for a real application, simply replace it with the sensor reading.
    '''

    global actual_temp

    min_temp_variation = 0
    max_temp_variation = 2
    temp_variation = round( random.uniform(min_temp_variation, max_temp_variation), 2)
    desviation_sense = random.randint(0,1)
    if desviation_sense:
        actual_temp = round(actual_temp - temp_variation, 2) #type: ignore
    else:
        actual_temp = round(actual_temp + temp_variation, 2) #type: ignore

    return str(actual_temp) + ' ' +  temp_unit #type: ignore
    
def get_hum():
    '''
     In this case, the function returns a random temperature value,
     but for a real application, simply replace it with the sensor reading.
    '''

    global actual_hum

    min_hum_variation = 0
    max_hum_variation = 5
    hum_variation = random.randint(min_hum_variation, max_hum_variation)
    desviation_sense = random.randint(0,1)
    if desviation_sense:
        actual_hum = actual_hum - hum_variation #type: ignore
    else:
        actual_hum = actual_hum + hum_variation #type: ignore

    return str(actual_hum) + hum_unit #type: ignore

def logging(message, path_to_file):
    print('[+]' + str(message))
    file = open(path_to_file, 'a')
    file.write(str(message) + '\n')
    file.close()

def send(type, message):
    '''
     Type = 0 --> temperature
     Type = 1 --> humidity
     Type = 2 --> power consumption
     Type = 3 --> people in zone
    '''

    if type == 0:
        message_to_send = 'Temp in ' + str(zone) + ' : ' + message #type: ignore 
        timestamp = time.time()
        logging(str(timestamp) + ' -> ' + message_to_send, temp_log) #type: ignore 
    elif type == 1:
        message_to_send = 'Hum in ' + str(zone) + ' : ' + message #type: ignore 
        timestamp = time.time()
        logging(str(timestamp) + ' -> ' + message_to_send, hum_log) #type: ignore 
    elif type == 2:
        message_to_send = 'Power in ' + str(zone) + ' : ' + message #type: ignore 
        timestamp = time.time()
        logging(str(timestamp) + ' -> ' + message_to_send, cons_log) #type: ignore 
    elif type == 3:
        message_to_send = 'People in ' + str(zone) + ' : ' + message #type: ignore 
        timestamp = time.time()
        logging(str(timestamp) + ' -> ' + message_to_send, counter_log) #type: ignore 
    else:
        print("[!]Unexpected type...")
    
    to_send = (message_to_send, timestamp)
    print(to_send) # Substitute for MQTT send code
    return True


class setInterval :
    def __init__(self,interval,action) :
        self.interval=interval
        self.action=action
        self.stopEvent=threading.Event()
        thread=threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            self.action()

    def cancel(self) :
        self.stopEvent.set()

def action_temp():
    send(0, get_temp())

def set_interval_temp(inter):
    if temp_interval != None:
        temp_interval.cancel()
        print('cancelled')
    aux_interval = setInterval(inter, action_temp)
    return aux_interval

def action_hum():
    send(1, get_hum())

def set_interval_hum(inter):
    global hum_interval
    if hum_interval != None:
        hum_interval.cancel()
        print('cancelled')
    aux_interval = setInterval(inter, action_hum)
    return aux_interval
