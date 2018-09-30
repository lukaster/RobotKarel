from tkinter import *
import os

import time


sleep_time = 0.75
tile_px_size = 50


direction = {
   0: "North",
   2: "South",
   3: "East",
    1: "West"
 }

class Game:

    def __init__(self,map):
        self.karel = map.karel
        self.map = map
        self.robot_label =  Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0, highlightthickness=0)

    def turn_left(self):
        self.karel.turn_left()
        print(self.karel.__str__())

    def is_in_front_of_the_wall(self):
        curr_x = self.karel.x
        curr_y = self.karel.y
        direction = self.karel.facing_directionInt
        result = False
        if direction == 0:
            if self.map.map_tiles[curr_y][curr_x].has_wall_N == True :
               result = True
            if curr_y > 0:
                if self.map.map_tiles[curr_y-1][curr_x].has_wall_S ==True:
                    result = True
            else:
                result = True
        if direction == 1:
            if self.map.map_tiles[curr_y][curr_x].has_wall_W ==True:
                result =True
            if curr_x > 0:
                if self.map.map_tiles[curr_y][curr_x-1].has_wall_E == True:
                    result = True
            else:
                result = True
        if direction == 2:
            if self.map.map_tiles[curr_y][curr_x].has_wall_S == True:
                result = True
            if curr_y < self.map.y_dim-1:
                 if self.map.map_tiles[curr_y + 1][curr_x].has_wall_N == True:
                      result = True
            else:
                result = True
        if direction == 3:
            if self.map.map_tiles[curr_y][curr_x].has_wall_E == True:
                result = True
            if curr_x < self.map.x_dim-1:
                if self.map.map_tiles[curr_y][curr_x + 1].has_wall_W == True:
                    result = True
            else:
                result = True
        if result==True:
            print("is in front of the wall")
        else:
            print("is NOT in front of the wall")
        return result

    def move(self):
        curr_x = self.karel.x
        curr_y = self.karel.y
        x_px_offset=12
        y_px_offset=8
        is_move_possible=True
        time.sleep(sleep_time)
        if self.is_in_front_of_the_wall() == False:
            direction = self.karel.facing_directionInt
            if direction == 0:
                self.karel.y = curr_y - 1
                self.map.map_tiles[curr_y][curr_x].has_robot = False
                self.map.map_tiles[curr_y-1][curr_x].has_robot = True
            if direction == 1:
                self.karel.x = curr_x - 1
                self.map.map_tiles[curr_y][curr_x].has_robot = False
                self.map.map_tiles[curr_y][curr_x-1].has_robot = True
            if direction == 2:
                self.karel.y = curr_y + 1
                self.map.map_tiles[curr_y][curr_x].has_robot = False
                self.map.map_tiles[curr_y + 1][curr_x].has_robot = True
            if direction == 3:
                self.karel.x = curr_x + 1
                self.map.map_tiles[curr_y][curr_x].has_robot = False
                self.map.map_tiles[curr_y][curr_x + 1].has_robot = True
            print(self.map.__str__())
            curr_x_px = self.karel.x * 50
            curr_y_px = self.karel.y * 50
            self.robot_label.destroy()
            self.robot_label = Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0, highlightthickness=0)
            self.robot_label.place(x=curr_x_px+x_px_offset, y=curr_y_px+y_px_offset)
            self.map.master.update()

    def is_on_beeper(self):
        print("is on beeper: {0}".format(self.map.map_tiles[self.karel.y][self.karel.x].has_beeper))
        return self.map.map_tiles[self.karel.y][self.karel.x].has_beeper


    def pick_up_beeper(self):
        if self.is_on_beeper() == True:
            if self.karel.has_beeper == False:
                self.karel.has_beeper = True
                self.map.map_tiles[self.karel.y][self.karel.x].has_beeper = False

    def put_down_beeper(self):
        if self.is_on_beeper() == False:
            if self.karel.has_beeper == True:
                self.karel.has_beeper = False
                self.map.map_tiles[self.karel.y][self.karel.x].has_beeper = True



class RobotKarel:

    def __init__(self,x,y,master):
        self.x = x
        self.y = y
        self.facing_directionInt = 0
        self.facing_directionStr = direction.get(self.facing_directionInt)
        self.has_beeper = False
        #dir_path = os.path.dirname(os.path.realpath(__file__))
        #print(dir_path)
        self.karel_picture = PhotoImage(file = "../robot_karel/karel.png")



    def turn_left(self):
        self.facing_directionInt = (self.facing_directionInt+1)%4
        self.facing_directionStr = direction.get(self.facing_directionInt)

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x:{0} y:{1}, facing {2}".format(self.x, self.y, self.facing_directionStr)


class MapTile:

    def __init__(self):
        self.has_beeper = False
        self.has_wall_N = False
        self.has_wall_S = False
        self.has_wall_E = False
        self.has_wall_W = False
        self.has_robot = False

    def put_wall(self, direction_where):
        if direction_where == 0:
            self.has_wall_N = True
        if direction_where == 1:
            self.has_wall_W = True
        if direction_where == 2:
            self.has_wall_S = True
        if direction_where == 3:
            self.has_wall_E = True

    def print_top(self):
        return "._ " if self.has_wall_N else ".   "

    def print_middle(self):
        middle = "  "
        wallL = " "
        wallR = " "
        if self.has_wall_W:
            wallL ="|"
        if self.has_wall_E:
            wallR = "|"
        if self.has_robot:
            middle = "R"
        if self.has_beeper:
            middle = "o"
        if self.has_beeper & self.has_robot:
            middle = "Ř"
        result = wallL+middle+wallR
        return result

    def print_bottom(self):
        return "._ " if self.has_wall_S else ".   "

    def __str__(self):
        return "x:{0} y:{1}, wall N {2}, W {3}, S {4}, E {5}, has Beeper {6}".format(self.x_coord,self.y_coord,self.has_wall_N,self.has_wall_W,self.has_wall_S,self.has_wall_E,self.has_beeper)


class WorldMap:

    def __init__(self, x_dim, y_dim, karel,master):
        self.x_dim = x_dim
        self.y_dim = y_dim

        self.map_tiles = [[0] * x_dim for i in range(y_dim)]
        self.background_image = None
        self.master = master

        for j in range(0, y_dim):
            for k in range(0, x_dim):
                self.map_tiles[j][k] = MapTile()
        self.map_tiles[karel.y][karel.x].has_robot = True
        self.karel = karel

   # def set_backgroud_picture_label(self,image_address):
    #    background = PhotoImage(file=image_address)
   #     self.background_label = Label(self.master, background, borderwidth=0, highlightthickness=0)

    def __str__(self):
        result = ""
        l = 0
        for j in range(0,self.y_dim):
            for l in range(0, 2):
                for k in range(0, self.x_dim):
                    if l == 0:
                        result = result + self.map_tiles[j][k].print_top()
                    if l == 1:
                        result = result + self.map_tiles[j][k].print_middle()
                    if l == 2:
                        result = result + self.map_tiles[j][k].print_bottom()
                if l != 1:
                    result = result + ".\n"
                else:
                    result = result + "\n"

        return result


class MapBuilder:

    def __init__(self,worldMap):
        self.map = worldMap

    def set_north_wall_to_tile(self,x,y):
        self.map.map_tiles[y][x].put_wall(0)
        if y>0:
            self.map.map_tiles[y-1][x].put_wall(2)
        return self

    def set_west_wall_to_tile(self, x, y):
        self.map.map_tiles[y][x].put_wall(1)
        if x > 0:
            self.map.map_tiles[y][x-1].put_wall(3)
        return self

    def set_south_wall_to_tile(self,x,y):
        self.map.map_tiles[y][x].put_wall(2)
        if self.map.y_dim - 1 > y:
            self.map.map_tiles[y+1][x].put_wall(0)
        return self

    def set_east_wall_to_tile(self,x,y):
        self.map.map_tiles[y][x].put_wall(3)
        if self.map.x_dim -1 > x:
            self.map.map_tiles[y][x + 1].put_wall(1)
        return self

    def set_robot(self,x,y):
        for j in range(0, self.map.y_dim):
            for k in range(0, self.map.x_dim):
                self.map.map_tiles[j][k].has_robot = False
        self.map.karel = RobotKarel(x,y)
        self.map.map_tiles[y][x].has_robot = True
        return self

    def set_beeper(self,x,y):
        self.map.map_tiles[y][x].has_beeper = True
        beeper = PhotoImage(file="../robot_karel/beeper.png")
        self.map.beeper_label = Label(self.map.master,image = beeper, borderwidth=0, highlightthickness=0)
        self.map.beeper_label.place(x=x*50+18, y=y*50+18)  # 16
        return self

    def build(self):
        print(self.map.__str__())
        return self.map
