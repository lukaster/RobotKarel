from RobotKarelGame.robot_karel_game import *
from RobotKarelGame.maps import *

root = Tk()
world_map = map_test_token(root)
karel = Game(world_map)
background_label = Label(root, image=karel.map.background_image, borderwidth=0, highlightthickness=0)
background_label.pack()
root.resizable(width=False, height=False)
karel.paint_init_conditions_on_background()


def move():
    karel.move()


def pick_up_beeper():
    karel.pick_up_beeper()


def turn_left():
    karel.turn_left()


def put_down_beeper():
    karel.put_down_beeper()


def is_in_front_of_wall():
    return karel.is_in_front_of_the_wall()


def is_on_beeper():
    return karel.is_on_beeper()


def is_on_green():
    return karel.is_on_green()


def is_on_purple():
    return karel.is_on_purple()
def has_beeper():
    return karel.has_beeper()

def token_value():
    return karel.token_value()

def ground_token_value():
    return karel.ground_token_value()

def is_on_token():
    return karel.is_on_token()

def pick_up_token():
    return karel.pick_up_token()

def put_down_token():
    return karel.put_down_token()
def has_token():
    return karel.has_token()

#################################################
# LIST OF COMMANDS
# Robot karel can:
#   STEP FORWARD -      move()
#   TURN LEFT -         turn_left()
#   PICK UP BEEPER -    pick_up_beeper()
#   PUT DOWN BEEPER -   put_down_beeper()
# Robot has sensors, it can tell you:
#   IF IT IS IN FRONT OF WALL -             is_in_front_of_wall()
#   IF IT IS STANDING ON TOP OF BEEPER -    is_on_beeper()
#################################################
# goal is to put both beepers to the right corner of the map
###your code here###
#################################################
def get_token_with_value(value):
    while 1:
        if is_on_token():
            if ground_token_value()==value:
                pick_up_token()
                break;
            else:
                move()
        else:
            move()

def turn_around():
    turn_left()
    turn_left()

def put_on_empty():
    while 1:
        move()
        if not is_on_token():
            put_down_token()
            break

def make_room():
    move()
    if is_on_token():
        pick_up_token()
        move()
        while is_on_token():
            move()
        put_down_token()
        turn_around()
        while is_on_token():
            move()
        turn_around()

""""""
for i in range(9,-1,-1):
    get_token_with_value(i)
    turn_around()
    put_on_empty()
    turn_around()
    make_room()
###end of your code###
#################################################
root.mainloop()