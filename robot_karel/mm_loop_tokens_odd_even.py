from RobotKarelGame.robot_karel_game import *
from RobotKarelGame.maps import *

root = Tk()
world_map = map_loop_tokens_odd_even(root)
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
def follow_wall_left():
    turn_left()
    if is_in_front_of_wall():
        turn_left()
        turn_left()
        turn_left()
        if is_in_front_of_wall():
            turn_left()
            turn_left()
            turn_left()
            move()
        else:
            move()
    else:
        move()

count = 0
turn_left()
turn_left()
move()
while count<6:
    follow_wall_left()
    if is_on_token() and not is_on_purple() and not is_on_green():
        pick_up_token()
    if is_on_green() and has_token() and token_value()%2==0 and not is_on_token():
        put_down_token()
        count = count+1
    else:
        if is_on_purple() and has_token() and token_value()%2!=0 and not is_on_token():
            put_down_token()
            count=count+1
    print("count {0}".format(count))

turn_left()
turn_left()
move()
turn_left()
move()
move()
turn_left()
"""
while 1:
    if is_in_front_of_wall():
        turn_left()
    else:
        move()
    if is_on_token():
        if has_token():
            karel.swap_tokens()
        else:
            pick_up_token()"""

###end of your code###
#################################################
root.mainloop()


