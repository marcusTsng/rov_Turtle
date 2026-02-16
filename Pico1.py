from machine import UART
uart1 = UART(1, baudrate=9600, tx=4, rx=5)
    
# USING FILE HANDLING
while True:
#     with open("/Users/marcustsang/Desktop/ROV/MainRepo/rov_Turtle/test.txt", "r") as f:
#         inp = f.read()
#         print(inp)
    x = input()
    if x:
        uart1.write(inp)
    
    
'''
Final decision
soooooo uhhhhhhhhhhhhh
claws: keyboard input, use autoclicker but for enter button (find online hopefully efficient)
movement: plug in controller ez

'''