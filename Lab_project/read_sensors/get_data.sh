cd $(dirname $0)

#configure w1 interface on gpio pins 5 and 6 for DS18b20 temperature sensors
dtoverlay w1-gpio gpiopin=5 pullup=0 >> setuplog.log 2>>setuplog.error
dtoverlay w1-gpio gpiopin=6 pullup=0 >> setuplog.log 2>>setuplog.error

echo $(date +%d.%m.%y-%H:%M): $(python read_sensors.py) $(./serial_read_arduino.out)  >> 2018.05.25.sensors_data.txt
