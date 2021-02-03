# Pico Play ![](images/GraphML.icon.png)
A few bits of _Raspberry Pi Pico_ sample code, borrowed from various places

## [MicroPython](https://micropython.org/)
<details>

* **Note:**
  * _MicroPython_ does not support USB HID
  * use _CircuitPython_ if you need to emulate a USB device

* [blink-irq.py](micro-python/blink-irq.py)
  * blink LED in PIO
  * PIO raises interrupt
  * interrupt is handled in a lambda
* [blink-pio.py](micro-python/blink-pio.py)
  * blink LED in PIO
* [blink-timer.py](micro-python/blink-timer.py)
  * blink (aka `toggle`) LED on a timer
* [blink-toggle.py](micro-python/blink-toggle.py)
  * toggle LED in a loop
* [hello.py](micro-python/hello.py)
  * canonical _Hello, world!_
* [pin-irq.py](micro-python/pin-irq.py)
  * TODO  test
* [pio-irq.py](micro-python/pio-irq.py)
  * PIO raises interrupt
  * interrupt is handled in a lambda
  * print interrupt flags
* [pio-pwm.py](micro-python/pio-pwm.py)
  * use PIO to implement PWM
  * fade LED using PWM
* [pwm.py](micro-python/pwm.py)
  * implement PWM in software
  * fade LED using PWM
* [temp.py](micro-python/temp.py)
  * print CPU temp in degrees C
  * reads analog pin
* [term-usb.py](micro-python/term-usb.py)
  * read characters from (USB) serial terminal
* [term-usb-temp.py](micro-python/term-usb-temp.py)
  * read characters from (USB) serial terminal
  * sends data (inc temp) to (USB) serial terminal
* [term-usb-temp-client.py](micro-python/term-usb-temp-client.py)
  * _Linux_ shell script to monitor (USB) serial terminal
  * companion program to Pico code above

</details>

## [CircuitPython](https://circuitpython.org/)
<details>

* **Note:**
  * _CircuitPython_ does not support interrupts by design
  * polling will probably be fast enough
  * will probably have to debounce inputs

* [blink-toggle.py](circuit-python/blink-toggle.py)
  * toggle LED in a loop
* [hello.py](circuit-python/hello.py)
  * canonical _Hello, world!_
* [hid-keyboard.py](circuit-python/hid-keyboard.py)
  * emulates USB keyboard
  * inserts character into active window - BEWARE!
  * should really be interrupt driven
* [hid-mouse.py](circuit-python/hid-mouse.py)
  * emulates USB mouse
  * moves mouse cursor
  * should really be interrupt driven
* [hid-usb.py](circuit-python/hid-usb.py)
  * lists available USB device emulations
* [list-pins.py](circuit-python/list-pins.py)
  * list pin designations on connected board
* [os.py](circuit-python/os.py)
  * output name of operating system
* [sys.py](circuit-python/sys.py)
  * output various system information
* [temp.py](circuit-python/temp.py)
  * print CPU temp in degrees C+F
  * directly reads CPU 'temperature'

</details>
