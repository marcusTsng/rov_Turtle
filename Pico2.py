# imports
import time
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
motor1 = PWM(Pin(6), freq=100, duty_ns=halt*ns)
motor2 = PWM(Pin(7), freq=100, duty_ns=halt*ns)
motor3 = PWM(Pin(9), freq=100, duty_ns=halt*ns)
motor4 = PWM(Pin(11), freq=100, duty_ns=halt*ns)
motor5 = PWM(Pin(12), freq=100, duty_ns=halt*ns)
motor6 = PWM(Pin(14), freq=100, duty_ns=halt*ns)
motors = {
    motor1, motor2, motor3, motor4, motor5, motor6  
}

# commands
def setMotor(motor, v)
    motor.init(freq=100, duty_ns = ns*(halt+v))
def move(v1, v2, v3, v4, v5, v6):
    setMotor(motor1, v1 * s)
    setMotor(motor2, v2 * s)
    setMotor(motor3, v3 * s)
    setMotor(motor4, v4 * s)
    setMotor(motor5, v5 * s)
    setMotor(motor6, v6 * s)
def brake(): pass
    for m in motors:
        setMotor(m, 0)
        #m.init(freq=100, duty_ns = ns*halt)
        
# runtime logic
cmd = None
while True:
    #if uart.any():
        #cmd = uart.read().decode('utf-8')
    cmd = input()
    if cmd: 
        if cmd == "z": led.toggle()
        elif cmd == "test": setMotor(motor1, 1) # only for testing, remove later
        elif cmd == "x": brake()
        elif cmd == "w": # FORWARD
            move(1, 0, -1, -1, 0, 1)
        elif cmd == "s": # BACKWARDS
            move(-1, 0, 1, 1, 0, -1)
        elif cmd == "a": # LEFT
            move(-1, 0, -1, 1, 0, 1)
        elif cmd == "d": # RIGHT
            move(1, 0, 1, -1, 0, -1)
        elif cmd == "i": # UP
            move(0, 1, 0, 0, 1, 0)
        elif cmd == "k": # DOWN
            move(0, -1, 0, 0, -1, 0)
        elif cmd == "l": # TURN CLOCKWISE
            move(-1, 0, 1, -1, 0, 1)
        elif cmd == "j": # TURN ANTICLOCKWISE
            move(1, 0, -1, 1, 0, -1)