#!/usr/bin/python
from tkinter import *
from RobotKarelGame.robot_karel_game import *
from RobotKarelGame.maps import *


import time

root = Tk()
world_map = map1(root)
game = Game(world_map)
background_label = Label(root,image=game.map.background_image, borderwidth=0, highlightthickness=0)
background_label.pack()
root.resizable(width=False, height=False)
#beeper = PhotoImage(file = "beeper.png")
#labelB = Label(root,image = beeper, borderwidth=0, highlightthickness=0)
#labelB.place(x=118,y=268)#16
#################################################
###your code here###
game.turn_left()
game.turn_left()
game.move()
game.move()
game.move()
game.turn_left()
game.move()
game.turn_left()
game.move()
game.turn_left()
game.move()
game.move()



##################################################
root.mainloop()#keep it on the screen

#pixel je 0.265mm