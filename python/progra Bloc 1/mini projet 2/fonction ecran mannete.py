import radio
import microbit
from microbit import *

# definition of functions
def get_message()-> str:
    """Wait and return a message from another micro:bit.
    
    Returns
    -------
    message: message sent by another micro:bit (str)
        
    """

    message = None    
    while message == None:
        microbit.sleep(250)
        message = radio.receive()
    
    return message


def screen_controller(local_view):
    """print the local map on the controller

    parameters
    ----------
    local_view: the information arround the player:str"""
    local_view = local_view.split()

    for i in range(5):
        x = int(local_view[i])
        y= int(local_view[i+1])
        for j in range(5):
             microbit.display.set_pixel(x, y, 9)

        
def tilt():
    """moves player based on tilt
    
    Returns
    -------
    tilt : the tilt of the micro:bit (str)
    """
    x = microbit.accelerometer.get_x() #get the value of x
    y = microbit.accelerometer.get_y() #get the value of y
    limit = 100
    
    if y> limit:
        return 'up'  #if the gamepad goes up
    elif y > limit: 
        return 'down'  #if the gamepad goes down
    elif x > limit:
        return 'right' #if the gamepad inclined on the right
    elif x < -limit:
        return 'left' #if the gamepad inclined on the left
    else:    
        return None #if the gamepad don't move, no move

def show_tilt(direction):
    """shows the player's movements on the micro:bit
    Parameter:
    -------
    direction : player's direction
    """
    if direction == 'up':
        display.show(Image.ARROW_N)
    elif direction == 'down':
        display.show( Image.ARROW_S)
    elif direction == 'left':
        display.show(Image.ARROW_W) 
    elif direction == 'right':
        display.show(Image.ARROW_E)
    
#setting
group_id = 24

# setup radio to receive/send messages
radio.on()
radio.config(group=group_id)

# loop forever (until micro:bit is switched off)
while True:
    # get local view of the board
    local_view = get_message()
    
    # clear screen
    microbit.display.clear()

    # show local view of the board 
    """ il faut resevoir un message de l'autre microbit (get_message) puis le transformer en parametre et le mettre dans la fonction 
    sCREEN CONTROLLER(mrssage)
    """
    # wait for button A to be pressed
    while not microbit.button_a.is_pressed():
        microbit.sleep(50)

    # send current direction
    direction = tilt()
    arrow = show_tilt(direction)

    radio.send(arrow)