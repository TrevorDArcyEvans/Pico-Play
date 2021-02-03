# https://hridaybarot.home.blog/2021/01/31/using-raspberry-pi-pico-has-hid-device-to-control-mouse-and-keyboard/
#
# Download or clone this repo:
#   https://github.com/adafruit/Adafruit_CircuitPython_HID
#
# In there, there is a folder called adafruit_hid ,
# copy that folder to the Pico where CircuitPython is already installed.

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

key_A = Keycode.A
key_Shift = Keycode.SHIFT
keyboard = Keyboard(usb_hid.devices)

time.sleep(2)
print("Sending keys now...")

keyboard.press(key_Shift, key_A)
keyboard.release(key_Shift, key_A)
