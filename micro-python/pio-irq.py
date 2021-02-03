# https://github.com/raspberrypi/pico-micropython-examples/blob/master/pio/pio_irq.py

import time
import rp2

@rp2.asm_pio()
def irq_test():
  wrap_target()

  nop() [31]
  nop() [31]
  nop() [31]
  nop() [31]
  irq(0)         # flags = 256

  nop() [31]
  nop() [31]
  nop() [31]
  nop() [31]
  irq(1)         # flags = 512

  nop() [31]
  nop() [31]
  nop() [31]
  nop() [31]
  irq(2)         # flags = 1024

  nop() [31]
  nop() [31]
  nop() [31]
  nop() [31]
  irq(3)         # flags = 2048

  wrap()

rp2.PIO(0).irq(lambda pio: print(pio.irq().flags()))

sm = rp2.StateMachine(0, irq_test, freq=1000)

sm.active(1)

time.sleep(1)

sm.active(0)
