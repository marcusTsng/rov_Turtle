"""
This is the first pico inside the ROV, which first recieves data from the tether.
Commands beginning in 0 command the thrusters, commands beginning in 1 are sent to the second pico.
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
def setMotor(motor, v):
def setMotor(motor, v):
    motor.init(freq=100, duty_ns = ns*(halt+v))
def move(v1, v2, v3, v4, v5, v6):
    setMotor(motor1, v1 * s)
    setMotor(motor2, v2 * s)
    setMotor(motor3, v3 * s)
    setMotor(motor4, v4 * s)
    setMotor(motor5, v5 * s)
    setMotor(motor6, v6 * s)
def brake(): 
def brake(): 
    for m in motors:
        setMotor(m, 0)
        #m.init(freq=100, duty_ns = ns*halt)
        
# runtime logic
cmd = None
while True:
    if uart.any():
        x = uart.read().decode('utf-8')
        if x[0] == "0": cmd = x
        elif x[0] == "1": pass # TRANSMIT TO OTHER PICO
    
    if cmd: 
        if cmd == "00": led.toggle()
        elif cmd == "tf": setMotor(motor1, 2) #TEST
        elif cmd == "tb": setMotor(motor1, -2) #TEST
        elif cmd == "ta": move(1, 1, 1, 1, 1, 1) #TEST
        elif cmd == "tab": move(-1, -1, -1, -1, -1, -1) #TEST
        elif cmd == "00": brake()
        elif cmd == "01": # FORWARD
            move(1, 0, -1, -1, 0, 1)
        elif cmd == "02": # BACKWARDS
            move(-1, 0, 1, 1, 0, -1)
        elif cmd == "03": # LEFT
            move(-1, 0, -1, 1, 0, 1)
        elif cmd == "04": # RIGHT
            move(1, 0, 1, -1, 0, -1)
        elif cmd == "05": # UP
            move(0, 1, 0, 0, 1, 0)
        elif cmd == "06": # DOWN
            move(0, -1, 0, 0, -1, 0)
        elif cmd == "07": # TURN CLOCKWISE
            move(-1, 0, 1, -1, 0, 1)
        elif cmd == "08": # TURN ANTICLOCKWISE
            move(1, 0, -1, 1, 0, -1)
            
brake()



## OLD CODE

# 
# from machine import UART
# uart1 = UART(1, baudrate=9600, tx=4, rx=5)
#     
# # USING FILE HANDLING
# while True:
# #     with open("/Users/marcustsang/Desktop/ROV/MainRepo/rov_Turtle/test.txt", "r") as f:
# #         inp = f.read()
# #         print(inp)
#     x = input()
#     if x:
#         uart1.write(inp)
#     
    
'''
Final decision
soooooo uhhhhhhhhhhhhh
claws: keyboard input, use autoclicker but for enter button (find online hopefully efficient)
movement: plug in controller ez

'''