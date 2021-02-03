import utime
from machine import Pin, Timer

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    utime.sleep(0.5)
    