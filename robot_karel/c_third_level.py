from RobotKarelGame.robot_karel_game import *
from RobotKarelGame.maps import *

root = Tk()
world_map = map_maze(root)
karel = Game(world_map)
#background_label = Label(root, image=karel.map.background_image, borderwidth=0, highlightthickness=0)
#background_label.pack()
newMap = PaintMap(root,world_map)
frame =newMap.frame
tiles_label_list = newMap.label_list
column_list =newMap.column_list
row_list = newMap.row_list

root.resizable(width=False, height=False)
karel.paint_init_conditions_on_background2(frame,tiles_label_list,column_list,row_list)
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
# goal is to find beeper in the maze and bring it back to the starting point
###your code here###
#################################################
def turn_right():
    for i in range(0,3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

count =0
move()
while 1:
    if is_on_beeper():
        pick_up_beeper()
    if is_on_green() and has_beeper():
        put_down_beeper()
        break
    turn_right()
    if is_in_front_of_wall():
        turn_left()
        if is_in_front_of_wall():
            turn_left()
            move()
        else:
            move()
    else:
        move()
    count=count+1

turn_around()
move()
for i in range(0,count):
    turn_left()
    if is_in_front_of_wall():
        turn_right()
        if is_in_front_of_wall():
            turn_right()
            move()
        else:
            move()
    else:
        move()
###end of your code###
#################################################
root.mainloop()