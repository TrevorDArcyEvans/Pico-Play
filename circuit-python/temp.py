# Measure, print, and plot outdoor temperature in C and F
#   https://forums.adafruit.com/viewtopic.php?f=60&t=174784&p=851901#p851901

import microcontroller
import time                                             

# CircuitPython does not have access to A04
sensor_temp = microcontroller.cpu[0].temperature             
fahrenheit = (sensor_temp * (9/5)) + 32

while True:
    print(fahrenheit)
    print(sensor_temp)
    print((fahrenheit, sensor_temp))
    time.sleep(2)
    