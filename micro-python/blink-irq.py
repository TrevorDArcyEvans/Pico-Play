import time
from machine import Pin
import rp2

@rp2.asm_pio(set_init = rp2.PIO.OUT_LOW)
def blink_1hz():
    # cycles: 1 + 1 + 6 + 32 * (30 + 1) = 1000
    irq(rel(0))
    set(pins, 1)
    set(x, 31)     [5]
    label("delay_high")
    nop()          [29]
    jmp(x_dec, "delay_high")
    
    # cycles: 1 + 7 + 32 * (30 + 1) = 1000
    set(pins, 0)
    set(x, 31)     [6]
    label("delay_low")
    nop()          [29]
    jmp(x_dec, "delay_low")
    
# create the StateMachine with the blink_1hz program, outputting on Pin(25)
sm = rp2.StateMachine(0, blink_1hz, freq = 2000, set_base = Pin(25))

# set the IRQ handler to print the millisecond timestamp
sm.irq(lambda p: print(int(time.ticks_ms()/1000)))

# start the StateMachine
sm.active(1)

time.sleep(10)

sm.active(0)
