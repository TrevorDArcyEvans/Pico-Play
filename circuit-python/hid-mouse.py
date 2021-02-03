# https://hridaybarot.home.blog/2021/01/31/using-raspberry-pi-pico-has-hid-device-to-control-mouse-and-keyboard/
#
# Download or clone this repo:
#   https://github.com/adafruit/Adafruit_CircuitPython_HID
#
# In there, there is a folder called adafruit_hid ,
# copy that folder to the Pico where CircuitPython is already installed.

import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

# This will move the mouse from it's current position by
# x pixels and y pixels. 
# So if the current position is (100,200), it'll move to
# (100+x,100+y)
x = 100
y = 100
mouse.move(x, y) 

