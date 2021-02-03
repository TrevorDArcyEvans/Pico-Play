import time
from machine import Pin
import rp2

@rp2.asm_pio(set_init = rp2.PIO.OUT_LOW)
def blink_1hz():
    # cycles: 1 + 1 + 6 + 32 * (30 + 1) = 1000
    irq(0)         # raises interrupt in StateMachine
    set(pins, 1)   # raises rising edge interrupt in Pin
    set(x, 31)     [5]
    label("delay_high")
    nop()          [29]
    jmp(x_dec, "delay_high")
    
    # cycles: 1 + 7 + 32 * (30 + 1) = 1000
    set(pins, 0)   # raises falling edge interrupt in Pin
    set(x, 31)     [6]
    label("delay_low")
    nop()          [29]
    jmp(x_dec, "delay_low")

sm = rp2.StateMachine(0, blink_1hz, freq = 2000, set_base = Pin(25))

print("Time  Src   (flags, trigger)")

# flags:
#   IRQ_RISING  --> 8
#   IRQ_FALLING --> 4
LED = Pin(25)
LED.irq(lambda pin:
    print(
        "{0:5d}".format(int(time.ticks_ms() / 1000)),
        "IRQ  ",
        (pin.irq().flags(), pin.irq().trigger())))

# flags:
#   OUT  --> 1
sm.irq(lambda p:
    print(
        "{0:5d}".format(int(time.ticks_ms() / 1000)),
        "SM   ",
        (p.irq().flags(), p.irq().trigger())))

# start the StateMachine
sm.active(1)

time.sleep(10)

sm.active(0)
