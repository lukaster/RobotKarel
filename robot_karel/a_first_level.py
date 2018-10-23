from RobotKarelGame.robot_karel_game import *
from RobotKarelGame.maps import *

root = Tk()
world_map = map1(root)
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

#################################################
#LIST OF COMMANDS
#Robot karel can:
#   STEP FORWARD -      move()
#   TURN LEFT -         turn_left()
#   PICK UP BEEPER -    pick_up_beeper()
#   PUT DOWN BEEPER -   put_down_beeper()
#Robot has sensors, it can tell you:
#   IF IT IS IN FRONT OF WALL -             is_in_front_of_wall()
#   IF IT IS STANDING ON TOP OF BEEPER -    is_on_beeper()
#################################################
# goal is to put both beepers to the right corner of the map
###your code here###
#################################################
def turn_right():
    for i in range(0,3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()
def move_n(n):
    for i in range(0, n):
        move()

turn_around()

if karel.is_on_green:
    move()

"""
turn_right()
while 1:
    if is_in_front_of_wall():
        turn_left()
    else:
        move()
        
if is_in_front_of_wall():
    move()
"""

"""
move()
turn_right()
move_n(3)
turn_left()
move_n(2)
pick_up_beeper()
turn_around()
move_n(2)
turn_left()
move_n(2)
put_down_beeper()
turn_around()
move_n(2)
turn_left()
move_n(3)
pick_up_beeper()
turn_around()
move_n(2)
turn_right()
move_n(2)
put_down_beeper()
"""
###end of your code###
#################################################
root.mainloop()