from machine import UART
uart1 = UART(1, baudrate=9600, tx=4, rx=5)

# USING TYPED INPUT
while True:
    uart1.write(input())
    
# USING FILE HANDLING
inp = ""
while inp != "!END!":
    with open("KEYS.txt", "w") as f:
        inp = f.read()
        f.write("")
    uart1.write(inp)