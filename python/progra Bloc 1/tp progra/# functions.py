# functions 
def move_forward():
    """make he robot move forward"""

    print("move forward")

def turn_right():
    """make the robot turn on the right"""
    
    print("turn right")

def turn_left():
    """make the robot turn on the left"""

    print("turn left")


move_forward()
turn_left()
turn_right()



def draw_square():
    """make the robot draw a square"""

    move_forward()
    turn_right()
    move_forward()

draw_square()
