# https://github.com/raspberrypi/pico-micropython-examples/blob/master/blink/blink.py

from machine import Pin, Timer

led = Pin(25, Pin.OUT)
tim = Timer()

def tick(timer):
    global led
    led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
