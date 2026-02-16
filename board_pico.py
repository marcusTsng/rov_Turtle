import sys, time
from machine import Pin, PWM, UART

led = Pin(25, Pin.OUT)

uart=UART(1, baudrate=9600, tx=4, rx=5)
uart.init(bits=8, parity=None, stop=1, timeout=1000)

while True:
    x = input()
    if x: uart.write(x)