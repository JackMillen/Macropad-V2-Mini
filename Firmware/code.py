# Macropad V2 (Mini)
# Jack Millen 2022

# Importing Libraries
import time
import board
from rainbowio import colorwheel
import neopixel
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from keypad import Event

# Initialising Keypad
km = keypad.KeyMatrix(
    column_pins=(board.D3, board.D4, board.D5, board.D6),
    row_pins=(board.D2, board.D1, board.D0),
)
kbd = Keyboard(usb_hid.devices)

# Neopixel Pins
pixel_pin = board.D7
num_pixels = 14

# Initialising NeoPixels
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False,)

# Initialising Key Combos
one = Event(0, True)
two = Event(1, True)
three = Event(2, True)
four = Event(3, True)
five = Event(4, True)
six = Event(5, True)
seven = Event(6, True)
eight = Event(7, True)
nine = Event(8, True)
ten = Event(9, True)
eleven = Event(10, True)
twelve = Event(11, True)

# Rainbow Animation
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        keypad()
        if cycle != 0:
            break
        time.sleep(wait)

# Changes light modes
global cycle
cycle = 0
def rgb_cycle():
    global cycle
    cycle += 1
    if cycle == 6:
        cycle = 0

# Keypad Outputs
def keypad():
    event = km.events.get()
    if event:
        if event == one:
            kbd.send(Keycode.F13)
            print("Button Pressed: 1")
        if event == two:
            kbd.send(Keycode.F14)
            print("Button Pressed: 2")
        if event == three:
            kbd.send(Keycode.F15)
            print("Button Pressed: 3")
        if event == four:
            kbd.send(Keycode.F16)
            print("Button Pressed: 4")
        if event == five:
            kbd.send(Keycode.F17)
            print("Button Pressed: 5")
        if event == six:
            kbd.send(Keycode.F18)
            print("Button Pressed: 6")
        if event == seven:
            kbd.send(Keycode.F19)
            print("Button Pressed: 7")
        if event == eight:
            kbd.send(Keycode.F20)
            print("Button Pressed: 8")
        if event == nine:
            print("Button Pressed: 9")
            rgb_cycle()
            print("RGB Mode: " + str(cycle))
        if event == ten:
            print("Button Pressed: 10")
            kbd.send(Keycode.F21)
        if event == eleven:
            print("Button Pressed: 11")
            kbd.send(Keycode.F22)
        if event == twelve:
            print("Button Pressed: 12")
            kbd.send(Keycode.F23)


# Main Loop
while True:
    if cycle == 0:
        rainbow_cycle(0.01)
    elif cycle == 1:
        keypad()
        pixels.fill((255, 0, 0))
        pixels.show()
    elif cycle == 2:
        keypad()
        pixels.fill((0, 255, 0))
        pixels.show()
    elif cycle == 3:
        keypad()
        pixels.fill((0, 0, 255))
        pixels.show()
    elif cycle == 4:
        keypad()
        pixels.fill((255, 255, 255))
        pixels.show()
    else:
        keypad()
        pixels.fill((0, 0, 0))
        pixels.show()
