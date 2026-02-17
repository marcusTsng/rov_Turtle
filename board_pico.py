"""
This is the pico on land which interprets the computer input
"""

import sys, time
from machine import Pin, PWM, UART

led = Pin(25, Pin.OUT)

uart=UART(1, baudrate=9600, tx=4, rx=5)
uart.init(bits=8, parity=None, stop=1, timeout=1000)

while True:
    x = input()
    if x:
        if x == "x": x = "00"
        elif x == "w": x = "01"
        elif x == "s": x = "02"
        elif x == "a": x = "03"
        elif x == "d": x = "04"
        elif x == "i": x = "05"
        elif x == "j": x = "06"
        elif x == "k": x = "07"
        elif x == "l": x = "08"
        uart.write(x)
    
"""
--KEY--

Test inputs: 
tf - Turns motor1 forwards
tb - Turns motor1 backwards
ta - Turns all motors forwards
tab - Turns all motors backwards

Thruster inputs:
X - 00, Brake
W - 01, Forwards
S - 02, Backwards 
A - 03, Left
D - 04, Right
I - 05, Up
J - 06, Down
K - 07, Turn clockwise
L - 08, Turn anticlockwise
"""