bypass = False

import digitalio
import board
import storage
from digitalio import DigitalInOut, Direction, Pull

# Setup the LED pin.
led = digitalio.DigitalInOut(board.D2)
led.direction = digitalio.Direction.OUTPUT

btn = DigitalInOut(board.D3)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

if not btn.value or bypass == True:
    print("Write Mode")
    storage.remount("/", True)
else:
    print("Read-Only Mode")
    storage.remount("/", False)
    storage.disable_usb_drive()

