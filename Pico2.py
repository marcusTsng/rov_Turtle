"""
This is the second pico in the ROV, which controls the arm.
Commands are sent from the first pico which instruct the arm movements.
"""

# imports
from machine import Pin, PWM, UART

# stuff
ns = 100000
halt = 15
s = 2


# led for testing
led = Pin(25, Pin.OUT)

# uart 
uart=UART(1, baudrate=9600, tx=4, rx=5)
uart.init(bits=8, parity=None, stop=1, timeout=1000)

# motors
servo1 = PWM(Pin(6), freq=100, duty_ns=halt*ns)



# commands
def setServo(servo, v):
    servo.init(freq=100, duty_ns = ns*(halt+v * s)) 
def brake(): 
    for s in servos:
        setServo(m, 0)
        #m.init(freq=100, duty_ns = ns*halt)
        
# runtime logic
cmd = None
while True:
#     if uart.any():
#         cmd = uart.read().decode('utf-8')
    cmd = input()
    if cmd: 
        if cmd == "10": led.toggle()
        elif cmd == "tf": setServo(servo1, 2) #TEST
        elif cmd == "tb": setServo(servo1, -2) # TEST
        
        elif cmd = "11": setServo(servo1, 1)
        elif cmd = "12": setServo(servo1, -1)
        elif cmd = "13": setServo(servo2, 1)
        elif cmd = "14": setServo(servo2, -1)
        elif cmd = "15": setServo(servo3, 1)
        elif cmd = "16": setServo(servo3, -1)
brake()