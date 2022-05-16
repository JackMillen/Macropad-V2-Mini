# Macropad-V2-Mini
![](/Pictures/Complete.jpg)
## What is this?
A PCB-based small form-factor USB keypad with RGB lighting

It consists of 12 Cherry Blue switches, 14 Neopixels, a tiny RP2040 and a custom PCB.
## What is the purpose of this project?
A few years ago I made [This](https://github.com/JackMillen/Macropad), a rough USB Macropad with 13 keys and 5 dials. This version has served me well and is perfect for a desktop, but leaves something to be desired when using it with a laptop.
## Issues with old version
- Too big to carry in a bag
- Too fragile (The wiring is held together with poor soldering, recycled wire and pure spite)
- The keys are misaligned due to sloppy 3D modelling
- Most of the dials do nothing because I don't use midi devices
- It uses USB Micro-B, not Type-C (which is superior in everway to lightning)
- It looks ugly
- Not enough RGB
- Handwiring sucks
## Solution?
Using a custom PCB, I can easily make a matrix of switches, while also integrating a strip of Neopixels into the rows. I can add pads on the bottom to solder a 
