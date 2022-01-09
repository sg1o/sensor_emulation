###############################################################################
#   ____ _    ____ ___  ____ _    _  _ ____ ____ _ ____ ___  _    ____ ____   #
#   | __ |    |  | |__] |__| |    |  | |__| |__/ | |__| |__] |    |___ [__    #
#   |__] |___ |__| |__] |  | |___  \/  |  | |  \ | |  | |__] |___ |___ ___]   #
#                                                                             #
###############################################################################


object_gui = None
zone = 1

'''Logging Files'''

temp_log = 'temperature_log.txt'
hum_log = 'humidity_log.txt'
cons_log = 'consumption_log.txt'
counter_log = 'person_in_zone_log.txt'

'''Variables for the people counter'''
people = 0
people_unit = 'people' # In this case unit is most a identifier in the message

'''Variables for power consumption'''
power_unit = 'kW'

'''Variables for temperature'''
actual_temp = 20
temp_unit = 'ºC'

'''Variable for humidity'''
actual_hum = 50
hum_unit = '%'


'''Intervals'''
temp_interval = None
hum_interval = None