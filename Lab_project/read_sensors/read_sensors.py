#!/usr/bin/python
#script that read two dht22 sensors on GPIO 19 and GPIO 13 and two ds18b20 water temperature sensors on GPIO 5 and 6
import sys
import os
import glob
import time
 
import RPi.GPIO as GPIO

#library for DHT22; use read_retry(22,<GPIO_PIN>) to read data
import Adafruit_DHT

#function to read ds18b20 water temperature sensor; uses w1 interface
def read_water_temperature(index):
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
     
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[index]
    device_file = device_folder + '/w1_slave'
     
    def read_temp_raw():
        try:
            f = open(device_file, 'r')
        except BaseException:
            sys.stderr.write("Cannot open ds18b20 sensor w1 interface device file!\n") 
        else:
            lines = f.readlines()
            f.close()
            return lines
     
    def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

    return read_temp()


ret_val = 0

#Initialize sensor data
temperature_1 = None
humidity_1 = None
water_temperature_1 = 0

temperature_2 = None
humidity_2 = None
water_temperature_2 = 0


#Sensor DHT22 GPIO 19
tries = 10
while (temperature_1 == None or humidity_1 == None) and tries > 0:
    humidity_1, temperature_1 = Adafruit_DHT.read_retry(22, 19)
    tries = tries - 1

#Water temp sensor GPIO 5
tries = 10
while water_temperature_1 == 0 and tries > 0:
    water_temperature_1 = read_water_temperature(0)
    tries = tries - 1

#Check if data makes sense, otherwise assign ERR to what doesn't make sense
if humidity_1 is None:
    humidity_1 = "ERR"
    ret_val = -1
else:
    humidity_1 = '{0:0.1f}'.format(humidity_1)

if temperature_1 is None:
    temperature_1 = "ERR"
    ret_val = -1
else:
    temperature_1 = '{0:0.1f}'.format(temperature_1)

if water_temperature_1 == 0:
    water_temperature_1 = "ERR"
    ret_val = -1
else:
    water_temperature_1 = '{0:0.1f}'.format(water_temperature_1)


#Sensor DHT22 GPIO 13
tries = 10
while (temperature_2 == None or humidity_2 == None) and tries > 0:
    humidity_2, temperature_2 = Adafruit_DHT.read_retry(22, 13)
    tries = tries - 1

#Water temp sensor GPIO 6
tries = 10
while water_temperature_2 == 0 and tries > 0:
    water_temperature_2 = read_water_temperature(1)
    tries = tries - 1


#Check if data makes sense, otherwise assign ERR to what doesn't make sense
if humidity_2 is None:
    humidity_2 = "ERR"
    ret_val = -1
else:
    humidity_2 = '{0:0.1f}'.format(humidity_2)

if temperature_2 is None:
    temperature_2 = "ERR"
    ret_val = -1
else:
    temperature_2 = '{0:0.1f}'.format(temperature_2)

if water_temperature_2 == 0:
    water_temperature_2 = "ERR"
    ret_val = -1
else:
    water_temperature_2 = '{0:0.1f}'.format(water_temperature_2)


#print data to stdout
sensors_string = temperature_1 + '\t' + humidity_1 + '\t' +  temperature_2 + '\t' + humidity_2 + '\t' + water_temperature_1 + ' \t' + water_temperature_2
print(sensors_string)


#exit with return value
sys.exit(ret_val)
