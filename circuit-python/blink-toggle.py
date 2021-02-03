import time
import board
from digitalio import DigitalInOut, Direction

# CircuitPython for Pico maps LED to GPIO25
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(1)
