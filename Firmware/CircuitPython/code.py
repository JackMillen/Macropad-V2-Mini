# Macropad V2 (Mini)
# Jack Millen 2022

# Importing Libraries
import time
import board
import math
import supervisor
import microcontroller
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
try:
    kbd = Keyboard(usb_hid.devices)
    hidActive = True
except:
    hidActive = False

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

# Rainbow Animation
def rainbow_fade(wait):
    for j in range(255):
        rc_index = j
        for i in range(num_pixels):
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        keypad()
        if cycle != 1:
            break
        time.sleep(wait)

# Red Fade
def red(wait, mult):
    for i in range(360*mult):
        keypad()
        value = ((((255 * math.sin(i/mult))//2) + (255//2))*0.8)+51
        pixels.fill((value, 0, 0))
        pixels.show()
        time.sleep(wait)
        if cycle != 2:
            break

# Green Fade
def green(wait, mult):
    for i in range(360*mult):
        keypad()
        value = ((((255 * math.sin(i/mult))//2) + (255//2))*0.8)+51
        pixels.fill((0, value, 0))
        pixels.show()
        time.sleep(wait)
        if cycle != 3:
            break

# Blue Fade
def blue(wait, mult):
    for i in range(360*mult):
        keypad()
        value = ((((255 * math.sin(i/mult))//2) + (255//2))*0.8)+51
        pixels.fill((0, 0, value))
        pixels.show()
        time.sleep(wait)
        if cycle != 4:
            break

# Yellow Fade
def yellow(wait, mult):
    for i in range(360*mult):
        keypad()
        value = ((((255 * math.sin(i/mult))//2) + (255//2))*0.8)+51
        pixels.fill((value, value, 0))
        pixels.show()
        time.sleep(wait)
        if cycle != 5:
            break

# Purple Fade
def purple(wait, mult):
    for i in range(360*mult):
        keypad()
        value = ((((255 * math.sin(i/mult))//2) + (255//2))*0.8)+51
        pixels.fill((value, 0, value))
        pixels.show()
        time.sleep(wait)
        if cycle != 6:
            break

# White Fade
def white(wait, mult):
    for i in range(360*mult):
        keypad()
        value = ((((255 * math.sin(i/mult))//2) + (255//2))*0.8)+51
        #print(""+str(value)+"")
        pixels.fill((value, value, value))
        pixels.show()
        time.sleep(wait)
        if cycle != 7:
            break

# Changes light modes
global cycle
global cycle_change
cycle_change = False
try:
    modeFile = open("mode.txt","r")
    cycle = int(modeFile.read())
    modeFile.close()
except:
    print("Can't Read From file")
    cycle = 0

def rgb_cycle():
    global cycle
    global cycle_change
    cycle_change = True
    cycle += 1
    if cycle == 8 + 1:
        cycle = 0

def write_cycle(cycle):
    try:
        modeFile = open("mode.txt","w")
        modeFile.write(str(cycle))
        modeFile.close()
    except:
        print("Can't Write to File")


# Keypad Outputs
def keypad():
    event = km.events.get()
    if hidActive:
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
    else:
        if event == nine:
            print("Button Pressed: 9")
            rgb_cycle()
            print("RGB Mode: " + str(cycle))


# Main Loop
while True:
    if cycle == 0:
        rainbow_cycle(0.01)
    elif cycle == 1:
        rainbow_fade(0.03)
    elif cycle == 2:
        red(0.03, 25)
    elif cycle == 3:
        green(0.03, 25)
    elif cycle == 4:
        blue(0.03, 25)
    elif cycle == 5:
        yellow(0.03, 25)
    elif cycle == 6:
        purple(0.03, 25)
    elif cycle == 7:
        white(0.03, 25)
    else:
        keypad()
        pixels.fill((0, 0, 0))
        pixels.show()

    if cycle_change:
        cycle_change = False
        write_cycle(cycle)
