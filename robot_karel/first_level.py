from RobotKarelGame.robot_karel_game import *
from RobotKarelGame.maps import *

root = Tk()
world_map = map1(root)
karel = Game(world_map)
background_label = Label(root, image=karel.map.background_image, borderwidth=0, highlightthickness=0)
background_label.pack()
root.resizable(width=False, height=False)
karel.paint_init_conditions_on_background()
#################################################
#LIST OF COMMANDS
#Robot karel can:
#   STEP FORWARD -      karel.move()
#   TURN LEFT -         karel.turn_left()
#   PICK UP BEEPER -    karel.pick_up_beeper()
#   PUT DOWN BEEPER -   karel.put_down_beeper()
#Robot has sensors, it can tell you:
#   IF IT IS IN FRONT OF WALL -             karel.is_in_front_of_the_wall()
#   IF IT IS STANDING ON TOP OF BEEPER -    karel.is_on_beeper()
#################################################
# goal is to put both beepers to the right corner of the map
###your code here###
#################################################



###end of your code###
#################################################
root.mainloop()