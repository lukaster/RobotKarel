from RobotKarelGame.robot_karel_game import *
from RobotKarelGame.maps import *

root = Tk()
world_map = map_maze(root)
game = Game(world_map)
background_label = Label(root,image=game.map.background_image, borderwidth=0, highlightthickness=0)
background_label.pack()
root.resizable(width=False, height=False)
game.paint_init_conditions_on_background()
#beeper = PhotoImage(file = "beeper.png")
#labelB = Label(root,image = beeper, borderwidth=0, highlightthickness=0)
#labelB.place(x=118,y=268)#16
#################################################
###your code here###




##################################################
root.mainloop()#keep it on the screen

#pixel je 0.265mm