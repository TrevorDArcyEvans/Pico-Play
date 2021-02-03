import usb_hid

# More info at:
#   https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf

print("(usage_page, usage)")
for dev in usb_hid.devices:
    print("  ", (dev.usage_page, dev.usage))


#(usage_page, usage)
#   (1, 6)  --> Desktop, Keyboard
#   (1, 2)  --> Desktop, Mouse
#   (12, 1) --> Consumer, ConsumerControl
#   (1, 5)  --> Desktop, Gamepad

# Other possible devices:
#   (1, 4)  --> Desktop, Joystick
#   (1, 7)  --> Desktop, Keypad
#   (12, 4) --> Consumer, Microphone
#   (12, 5) --> Consumer, Headphone
