#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
from init import *
import func

#general functions
#################
#display function
def draw_screen():
    message_string = panels[panel_number] + '  ' + value_top_left + r'  ' + value_top_right + r' >' + '\n' + \
                     panel + value_bottom_left + r'  ' + value_bottom_right + r' <'
    lcd.clear()
    lcd.message(message_string)

#get sensor data from file function
def get_data():
    global last_measurement
    with open(sensors_data_file) as sensors_data:
        last_measurement = (sensors_data.readlines())[-1].split(" ")


#callback functions
####################
#panel select button
def handle_top_left(pin):
    global panel_number
    global value_top_left  
    global value_top_right
    global value_bottom_left 
    global value_bottom_right 
    if panel_number == PH_panel :
        if reading == 0 :
            #switch to TH_panel
            panel_number       =  TH_panel 
            value_top_left     =  T_value[0]
            value_top_right    =  T_value[1]
            value_bottom_left  =  H_value[0]
            value_bottom_right =  H_value[1]
    if panel_number == RD_panel : 
            #turn off blink cursor
            reading = 0
            if reading == 1 or reading == 2 :
                lcd.set_cursor(3, 0)

            value_top_left     = PH_value[0]
            value_top_right    = PH_value[1]
            value_bottom_left  = PH_value[2]
            value_bottom_right = PH_value[3]
     
    if panel_number == TH_panel :
        #switch to WT panel
        panel_number       = WT_panel 
        value_top_left     = WT_value[0]
        value_top_right    = WT_value[1]
        value_bottom_left  = 0
        value_bottom_right = 0
    if panel_number == WT_panel :
        #switch to LS panel
        panel_number       = LS_panel 
        value_top_left     = LS_value[0]
        value_top_right    = LS_value[1]
        value_bottom_left  = LS_value[2]
        value_bottom_right = LS_value[3]
    if panel_number == LS_panel :
        #switch to EC panel
        panel_number       = EC_panel
        value_top_left     = EC_value[0]
        value_top_right    = EC_value[1]
        value_bottom_left  = EC_value[2]
        value_bottom_right = EC_value[3]
    if panel_number == EC_panel :
        #switch to PH panel
        panel_number       = PH_panel
        value_top_left     = PH_value[0]
        value_top_right    = PH_value[1]
        value_bottom_left  = PH_value[2]
        value_bottom_right = PH_value[3]
        #turn on cursor
        lcd.show_cursor
    draw_screen()

#SL button
def handle_bottom_left(pin):
    global message_string
    message_string = 'bottom_left'
    draw_screen()

#> button
def handle_top_right(pin):
    global message_string
    message_string = 'top_right'
    draw_screen()

#< button
def handle_bottom_right(pin):
    global message_string
    message_string = 'bottom_right'
    draw_screen()


#setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup([button_top_left, button_bottom_left, button_top_right, button_bottom_right], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)


#setup GPIO callbacks
GPIO.add_event_detect(button_top_left, GPIO.RISING, handle_top_left)
GPIO.add_event_detect(button_bottom_left, GPIO.RISING, handle_bottom_left)
GPIO.add_event_detect(button_top_right, GPIO.RISING, handle_top_right)
GPIO.add_event_detect(button_bottom_right, GPIO.RISING, handle_bottom_right)

while True:
    #get sensor data to be used to display
    get_data()
    time.sleep(360)


#lcd.clear()
#lcd.show_cursor(True)


#lcd.blink(True)
#lcd.message('Blink cursor')


#lcd.show_cursor(False)
#lcd.blink(False)

