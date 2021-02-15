# https://github.com/adafruit/Adafruit_CircuitPython_HID

import usb_hid
from adafruit_hid.gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

# Test on Linux with:
#   jstest-gtk
#   https://jstest-gtk.gitlab.io/

# click gamepad buttons
# button index is 1-based
# icons in jstest-gtk will flash briefly
gp.click_buttons(1, 3, 4, 7)

# move joysticks in range [-127, 127]
# jstest-gtk maps to [-32767, 32767]
gp.move_joysticks(x = 90, y = 70, z = -80, r_z = 60)
