from machine import Pin, PWM, UART
import time

# --- CONFIGURATION ---
MOTOR_PINS = [0, 1, 2, 3, 4, 5] 

motors = []
for pin in MOTOR_PINS:
    pwm = PWM(Pin(pin))
    pwm.freq(50)
    pwm.duty_u16(4915) 
    motors.append(pwm)

uart = UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))
last_heartbeat = time.ticks_ms()

def set_thruster(index, thrust):
    # Cap the raw math between -1.0 and 1.0 just to be safe
    thrust = max(-1.0, min(1.0, thrust)) 
    
    # 1500 is neutral. Max forward is now 1500 + 300 = 1800us (1.8ms)
    # Max reverse is now 1500 - 300 = 1200us (1.2ms)
    us = 1500 + (thrust * 300)
    
    # Convert that microsecond target into a 16-bit duty cycle for the Pico
    duty = int((us / 20000) * 65535)
    motors[index].duty_u16(duty)

def mix_and_drive(forward, turn, vertical, roll):
    # --- HORIZONTAL MOTORS (Joystick 1: Forward & Turning) ---
    m1 = forward - turn  # Front-Right
    m2 = forward + turn  # Front-Left
    m3 = forward - turn  # Rear-Right
    m4 = forward + turn  # Rear-Left

    # Normalize horizontal motors so they don't exceed 100%
    max_horiz = max(abs(m1), abs(m2), abs(m3), abs(m4), 1.0)
    set_thruster(0, -m1 / max_horiz) # GP0
    set_thruster(1, m2 / max_horiz) # GP1
    set_thruster(2, m3 / max_horiz) # GP2
    set_thruster(3, -m4 / max_horiz) # GP3
    
    # --- VERTICAL MOTORS (Joystick 2: Up/Down & Rolling) ---
    # Assuming GP4 is the LEFT vertical motor, GP5 is the RIGHT vertical motor
    v1 = vertical + roll # Left Vertical
    v2 = vertical - roll # Right Vertical
    
    # Normalize vertical motors so they don't exceed 100%
    max_vert = max(abs(v1), abs(v2), 1.0)
    set_thruster(4, v1 / max_vert) # GP4
    set_thruster(5, v2 / max_vert) # GP5

def stop_all_motors():
    for i in range(6):
        set_thruster(i, 0.0)

# --- MAIN LOOP ---
print("Wetside Pico Ready. Airplane logic active...")

while True:
    if uart.any():
        try:
            line = uart.readline().decode('utf-8').strip()
            data = line.split(',')
            
            # Expecting the exact same 4-element array from the PC!
            if len(data) == 4:
                # Joystick 1 (Elements 0 & 1)
                forward = float(data[0]) 
                turn = float(data[1])    
                
                # Joystick 2 (Elements 2 & 3)
                vertical = float(data[2])
                roll = float(data[3])    
                
                mix_and_drive(forward, turn, vertical, roll)
                last_heartbeat = time.ticks_ms()
                
        except Exception:
            pass
            
    # FAILSAFE
    if time.ticks_diff(time.ticks_ms(), last_heartbeat) > 1000:
        stop_all_motors()
        
    time.sleep(0.01)
