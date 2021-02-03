import utime
from rp2 import PIO, asm_pio
from machine import Pin

# Define the blink program.  It has one GPIO to bind to on the set instruction, which is an output pin.
# Use lots of delays to make the blinking visible by eye.
@asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()

# Instantiate a state machine with the blink program,
# at 1000Hz, with set bound to Pin(25) (LED on the rp2 board)
sm = rp2.StateMachine(0, blink, freq=1000, set_base=Pin(25))

# Run the state machine for 3 seconds.  The LED should blink.
sm.active(1)

utime.sleep(3)

sm.active(0)