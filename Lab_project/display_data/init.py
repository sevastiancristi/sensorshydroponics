# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight =  4
lcd_columns   = 16

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    =  2

#buttons defintion
button_top_left     = 21 
button_bottom_left  = 20
button_top_right    = 16
button_bottom_right = 12

#initial print values
value_top_left     = 0
value_bottom_left  = 0
value_top_right    = 0
value_bottom_right = 0

#panels definition
panels = ["TH", "WT" ,"EC" , "LS", "PH", "RD"]
panel_number = 0
TH_panel = 0
WT_panel = 1
EC_panel = 2
LS_panel = 3
PH_panel = 4
RD_panel = 5

#indices for last_measurement array
T_ind  = [ 1, 3]
H_ind  = [ 2, 4]
WT_ind = [ 5, 6]
LS_ind = [ 7, 8, 9,10]
EC_ind = [11,12,13,14]
PH_ind = [15,16,17,18]

#initial values of sensor values
T_value  = [ 0, 0]
H_value  = [ 0, 0]
WT_value = [ 0, 0]
LS_value = [ 0, 0, 0, 0]
EC_value = [ 0, 0, 0, 0]
PH_value = [ 0, 0, 0, 0]

#last measurement
last_measurement = []

#path to sensor data file
sensors_data_file = "../read_sensors/2018.05.25.sensors_data.txt"

