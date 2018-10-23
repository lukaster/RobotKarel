from tkinter import *
import time


sleep_time = 0.01
tile_px_size = 50
x_px_offset = 8
y_px_offset = 8

direction = {
   0: "North",
   2: "South",
   3: "East",
    1: "West"
 }
karel_basic_addres ={
    0: "../RobotKarelGame/pictures/karel/karelBasic/karelN.png",
    2: "../RobotKarelGame/pictures/karel/karelBasic/karelS.png",
    3: "../RobotKarelGame/pictures/karel/karelBasic/karelE.png",
    1: "../RobotKarelGame/pictures/karel/karelBasic/karelW.png"
}
karel_picture_states = { # 0 no beeper, 1 has something
    0: {    0:{     0: "../RobotKarelGame/pictures/karel/karelBasic/karelN.png",
                    2: "../RobotKarelGame/pictures/karel/karelBasic/karelS.png",
                    3: "../RobotKarelGame/pictures/karel/karelBasic/karelE.png",
                    1: "../RobotKarelGame/pictures/karel/karelBasic/karelW.png"}},
    1: {    1:{     0: "../RobotKarelGame/pictures/karel/KarelBeeper/karel_beeperN.png",#0token,1beeper
                    2: "../RobotKarelGame/pictures/karel/KarelBeeper/karel_beeperS.png",
                    3: "../RobotKarelGame/pictures/karel/KarelBeeper/karel_beeperE.png",
                    1: "../RobotKarelGame/pictures/karel/KarelBeeper/karel_beeperW.png"},
            0:      {0: "../RobotKarelGame/pictures/karel/karelToken/karelN.png",
                    2: "../RobotKarelGame/pictures/karel/karelToken/karelS.png",
                    3: "../RobotKarelGame/pictures/karel/karelToken/karelE.png",
                    1: "../RobotKarelGame/pictures/karel/karelToken/karelW.png"}
            }
}

token_values_pictures = {
    0: "../RobotKarelGame/pictures/tokens/token_0.png",
    1: "../RobotKarelGame/pictures/tokens/token_1.png",
    2: "../RobotKarelGame/pictures/tokens/token_2.png",
    3: "../RobotKarelGame/pictures/tokens/token_3.png",
    4: "../RobotKarelGame/pictures/tokens/token_4.png",
    5: "../RobotKarelGame/pictures/tokens/token_5.png",
    6: "../RobotKarelGame/pictures/tokens/token_6.png",
    7: "../RobotKarelGame/pictures/tokens/token_7.png",
    8: "../RobotKarelGame/pictures/tokens/token_8.png",
    9: "../RobotKarelGame/pictures/tokens/token_9.png",
}

class Game:

    def __init__(self,map):
        self.karel = map.karel
        self.map = map
        self.robot_label =  Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0, highlightthickness=0)
        self.beeper_picture = { # 0 blue, 1 green, 2 purple
            0: PhotoImage(file="../RobotKarelGame/pictures/beepers/beeper_b.png"),
            1: PhotoImage(file="../RobotKarelGame/pictures/beepers/beeper_g.png"),
            2: PhotoImage(file="../RobotKarelGame/pictures/beepers/beeper_p.png"),
        }
        self.beeper_label_list = []
        self.token_label_list = []
        self.frame = NONE
        self.background_label_list = []
        self.background_label_column_list = []
        self.background_label_row_list = []


    def paint_init_conditions_on_background(self):
        #painted_map = paint_map.PaintMap(self.map.master, self.map)
        #self.background_label_list=painted_map.label_list
        self.map.karel.karel_picture = PhotoImage(
            file=karel_picture_states.get(self.map.karel.has_beeper or self.map.karel.has_token).get(self.map.karel.has_beeper).get(self.karel.facing_directionInt))
        self.robot_label = Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0,highlightthickness=0)
        self.robot_label.place(x=self.karel.x * tile_px_size + x_px_offset, y=self.karel.y * tile_px_size + y_px_offset)
        for i in range(0,len(self.map.beeper_x_coord_list)):
            self.beeper_label_list.append(Label(self.map.master, image=self.beeper_picture.get(self.map.map_tiles[self.map.beeper_y_coord_list[i]][self.map.beeper_x_coord_list[i]].color), borderwidth=0, highlightthickness=0))
            self.beeper_label_list[i].place(x=self.map.beeper_x_coord_list[i] * tile_px_size + 18, y=self.map.beeper_y_coord_list[i] * tile_px_size + 18)  # 16
        for i in range(0, len(self.map.token_x_coord_list)):
            self.token_label_list.append(Label(self.map.master, image=self.map.map_tiles[self.map.token_y_coord_list[i]][self.map.token_x_coord_list[i]].token.picture, borderwidth=0, highlightthickness=0))
            self.token_label_list[i].place(x=self.map.token_x_coord_list[i] * tile_px_size + 12, y=self.map.token_y_coord_list[i] * tile_px_size + 12)  # 16
        self.map.master.update()

    def paint_init_conditions_on_background2(self, frame,tiles_label_list,column_list,row_list):
        self.frame = frame
        self.background_label_list=tiles_label_list
        self.background_label_column_list = column_list
        self.background_label_row_list = row_list
        self.frame.pack()
        for i in range(0,len(self.background_label_list)):
            self.background_label_list[i].grid(row = row_list[i],column = column_list[i])

        # painted_map = paint_map.PaintMap(self.map.master, self.map)
        # self.background_label_list=painted_map.label_list
        self.map.karel.karel_picture = PhotoImage(
            file=karel_picture_states.get(self.map.karel.has_beeper or self.map.karel.has_token).get(
                self.map.karel.has_beeper).get(self.karel.facing_directionInt))
        self.robot_label = Label(self.frame, image=self.map.karel.karel_picture, borderwidth=0,
                                 highlightthickness=0)
        self.robot_label.place(x=self.karel.x * tile_px_size + x_px_offset,
                               y=self.karel.y * tile_px_size + y_px_offset)
        for i in range(0, len(self.map.beeper_x_coord_list)):
            self.beeper_label_list.append(Label(self.frame, image=self.beeper_picture.get(
                self.map.map_tiles[self.map.beeper_y_coord_list[i]][self.map.beeper_x_coord_list[i]].color),
                                                borderwidth=0, highlightthickness=0))
            self.beeper_label_list[i].place(x=self.map.beeper_x_coord_list[i] * tile_px_size + 18,
                                            y=self.map.beeper_y_coord_list[i] * tile_px_size + 18)  # 16
        for i in range(0, len(self.map.token_x_coord_list)):
            self.token_label_list.append(Label(self.frame,
                                               image=self.map.map_tiles[self.map.token_y_coord_list[i]][
                                                   self.map.token_x_coord_list[i]].token.picture, borderwidth=0,
                                               highlightthickness=0))
            self.token_label_list[i].place(x=self.map.token_x_coord_list[i] * tile_px_size + 12,
                                           y=self.map.token_y_coord_list[i] * tile_px_size + 12)  # 16
        self.map.master.update()

    def turn_left(self):
        self.karel.turn_left()
        time.sleep(sleep_time)
        self.robot_label.destroy()
        self.map.karel.karel_picture= PhotoImage( file=karel_picture_states.get(self.map.karel.has_beeper or self.map.karel.has_token).get(self.map.karel.has_beeper).get(self.karel.facing_directionInt))
        self.robot_label = Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0,highlightthickness=0)
        self.robot_label.place(x=self.karel.x * tile_px_size + x_px_offset, y=self.karel.y * tile_px_size + y_px_offset)
        self.map.master.update()
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

    def is_on_token(self):
        return self.map.map_tiles[self.karel.y][self.karel.x].has_token

    def is_on_green(self):
        return self.map.map_tiles[self.karel.y][self.karel.x].color==1

    def is_on_purple(self):
        return self.map.map_tiles[self.karel.y][self.karel.x].color==2

    def has_beeper(self):
        return self.map.karel.has_beeper

    def has_token(self):
        return self.map.karel.has_token

    def token_value(self):
        return self.map.karel.token.value

    def ground_token_value(self):
        if self.is_on_token():
            return self.map.map_tiles[self.map.karel.y][self.map.karel.x].token.value
        else:
            print("not currently standing on any token")

    def pick_up_beeper(self):
        if self.is_on_beeper() == True:
            if self.karel.has_beeper == False:
                self.karel.has_beeper = True
                self.map.map_tiles[self.karel.y][self.karel.x].has_beeper = False
                #finds the beeper label corresponding to place where karel is and deletes it
                for i in range(0,len(self.map.beeper_x_coord_list)):
                    if self.karel.x == self.map.beeper_x_coord_list[i] and self.karel.y == self.map.beeper_y_coord_list[i]:
                        self.beeper_label_list[i].destroy()
                        del self.beeper_label_list[i]
                        del self.map.beeper_x_coord_list[i]
                        del self.map.beeper_y_coord_list[i]
                        self.map.master.update()
                        break
        #puts new picture of karel
        self.robot_label.destroy()
        time.sleep(sleep_time)
        self.map.karel.karel_picture = PhotoImage( file=karel_picture_states.get(self.map.karel.has_beeper or self.map.karel.has_token).get(self.map.karel.has_beeper).get(self.karel.facing_directionInt))
        self.robot_label = Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0,highlightthickness=0)
        self.robot_label.place(x=self.karel.x * tile_px_size + x_px_offset,y=self.karel.y * tile_px_size + y_px_offset)
        self.map.master.update()

    def put_down_beeper(self):
        if self.is_on_beeper() == False:
            if self.karel.has_beeper == True:
                self.karel.has_beeper = False
                self.map.map_tiles[self.karel.y][self.karel.x].has_beeper = True
                #picture update
                time.sleep(sleep_time)
                self.map.beeper_x_coord_list.append(self.karel.x)
                self.map.beeper_y_coord_list.append(self.karel.y)
                self.robot_label.destroy()
                self.beeper_label_list.append(Label(self.map.master, image=self.beeper_picture.get(self.map.map_tiles[self.karel.y][self.karel.x].color), borderwidth=0, highlightthickness=0))
                self.beeper_label_list[-1].place(x=self.karel.x  * tile_px_size + 18,y=self.karel.y  * tile_px_size + 18)  # 16
                self.map.karel.karel_picture = PhotoImage( file=karel_picture_states.get(self.map.karel.has_beeper or self.map.karel.has_token).get(self.map.karel.has_beeper).get(self.karel.facing_directionInt))
                self.robot_label = Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0,highlightthickness=0)
                self.robot_label.place(x=self.karel.x * tile_px_size + x_px_offset,y=self.karel.y * tile_px_size + y_px_offset)
                self.map.master.update()
                time.sleep(sleep_time/5)


    def pick_up_token(self):
        if self.is_on_token() == True:
            if self.karel.has_token == False:
                self.karel.has_token = True
                self.karel.token = self.map.map_tiles[self.karel.y][self.karel.x].token
                self.map.map_tiles[self.karel.y][self.karel.x].token=NONE
                self.map.map_tiles[self.karel.y][self.karel.x].has_token = False
                #finds the beeper label corresponding to place where karel is and deletes it
                for i in range(0,len(self.map.token_x_coord_list)):
                    if self.karel.x == self.map.token_x_coord_list[i] and self.karel.y == self.map.token_y_coord_list[i]:
                        self.token_label_list[i].destroy()
                        del self.token_label_list[i]
                        del self.map.token_x_coord_list[i]
                        del self.map.token_y_coord_list[i]
                        self.map.master.update()
                        break
        #puts new picture of karel
        self.robot_label.destroy()
        time.sleep(sleep_time)
        self.map.karel.karel_picture = PhotoImage( file=karel_picture_states.get(self.map.karel.has_beeper or self.map.karel.has_token).get(self.map.karel.has_beeper).get(self.karel.facing_directionInt))
        self.robot_label = Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0,highlightthickness=0)
        self.robot_label.place(x=self.karel.x * tile_px_size + x_px_offset,y=self.karel.y * tile_px_size + y_px_offset)
        self.map.master.update()

    def put_down_token(self):
        if self.is_on_token() == False:
            if self.karel.has_token == True:
                self.karel.has_token = False
                self.map.map_tiles[self.karel.y][self.karel.x].has_token = True
                self.map.map_tiles[self.karel.y][self.karel.x].token=self.karel.token
                self.karel.token=NONE
                #picture update
                time.sleep(sleep_time)
                self.map.token_x_coord_list.append(self.karel.x)
                self.map.token_y_coord_list.append(self.karel.y)
                self.robot_label.destroy()
                self.token_label_list.append(Label(self.map.master, image=self.map.map_tiles[self.karel.y][self.karel.x].token.picture, borderwidth=0, highlightthickness=0))
                self.token_label_list[-1].place(x=self.karel.x  * tile_px_size + 12,y=self.karel.y  * tile_px_size + 12)  # 16
                self.map.karel.karel_picture = PhotoImage( file=karel_picture_states.get(self.map.karel.has_beeper or self.map.karel.has_token).get(self.map.karel.has_beeper).get(self.karel.facing_directionInt))
                self.robot_label = Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0,highlightthickness=0)
                self.robot_label.place(x=self.karel.x * tile_px_size + x_px_offset,y=self.karel.y * tile_px_size + y_px_offset)
                self.map.master.update()
                time.sleep(sleep_time/5)

    def swap_tokens(self):
        if self.is_on_token() == True:
            if self.karel.has_token == True:
                tmp_token = self.map.map_tiles[self.karel.y][self.karel.x].token
                self.map.map_tiles[self.karel.y][self.karel.x].token=self.karel.token
                self.karel.token=tmp_token
                #picture update
                time.sleep(sleep_time)
                #finds the beeper label corresponding to place where karel is and deletes it
                for i in range(0,len(self.map.token_x_coord_list)):
                    if self.karel.x == self.map.token_x_coord_list[i] and self.karel.y == self.map.token_y_coord_list[i]:
                        self.token_label_list[i].destroy()
                        del self.token_label_list[i]
                        del self.map.token_x_coord_list[i]
                        del self.map.token_y_coord_list[i]
                        self.map.master.update()
                        break
                self.map.token_x_coord_list.append(self.karel.x)
                self.map.token_y_coord_list.append(self.karel.y)
                #animate karel swap
                self.karel.has_token=False
                self.robot_label.destroy()
                self.robot_label = Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0,highlightthickness=0)
                self.robot_label.place(x=self.karel.x * tile_px_size + x_px_offset,y=self.karel.y * tile_px_size + y_px_offset)
                self.map.master.update()
                time.sleep(sleep_time / 15)

                self.karel.has_token=True
                self.robot_label.destroy()
                self.token_label_list.append(Label(self.map.master, image=self.map.map_tiles[self.karel.y][self.karel.x].token.picture, borderwidth=0, highlightthickness=0))
                self.token_label_list[-1].place(x=self.karel.x  * tile_px_size + 12,y=self.karel.y  * tile_px_size + 12)  # 16
                self.map.karel.karel_picture = PhotoImage( file=karel_picture_states.get(self.map.karel.has_beeper or self.map.karel.has_token).get(self.map.karel.has_beeper).get(self.karel.facing_directionInt))
                self.robot_label = Label(self.map.master, image=self.map.karel.karel_picture, borderwidth=0,highlightthickness=0)
                self.robot_label.place(x=self.karel.x * tile_px_size + x_px_offset,y=self.karel.y * tile_px_size + y_px_offset)
                self.map.master.update()
                time.sleep(sleep_time/5)



class RobotKarel:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.facing_directionInt = 0
        self.facing_directionStr = direction.get(self.facing_directionInt)
        self.has_beeper = False
        self.karel_picture = PhotoImage(file = "../RobotKarelGame/pictures/karel/karelBasic/karelN.png")
        self.has_token = False
        self.token = NONE

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
        self.color = 0 #0 blue,1 green,2 purple
        self.has_token = False
        self.token = NONE

    def put_wall(self, direction_where):
        if direction_where == 0:
            self.has_wall_N = True
        if direction_where == 1:
            self.has_wall_W = True
        if direction_where == 2:
            self.has_wall_S = True
        if direction_where == 3:
            self.has_wall_E = True

    def put_token(self, token):
        if not self.has_token:
            self.has_token = True
            self.token = token
            return True
        else:
            return False

    def give_token(self):
        if self.has_token:
            token = self.token
            self.token = NONE
            self.has_token=False
            return token


    def set_color(self,color):
        self.color=color

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
        if self.has_token:
            middle = "T"
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

        self.beeper_x_coord_list=[]
        self.beeper_y_coord_list=[]

        self.token_x_coord_list =[]
        self.token_y_coord_list =[]

        for j in range(0, y_dim):
            for k in range(0, x_dim):
                self.map_tiles[j][k] = MapTile()
        self.map_tiles[karel.y][karel.x].has_robot = True
        self.karel = karel

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

    def set_south_wall_to_tiles_from_to(self, x_from,x_to, y):
        for i in range(x_from,x_to+1):
            self.map.map_tiles[y][i].put_wall(2)
            if self.map.y_dim - 1 > y:
                self.map.map_tiles[y+1][i].put_wall(0)
        return self

    def set_east_wall_to_tile(self,x,y):
        self.map.map_tiles[y][x].put_wall(3)
        if self.map.x_dim -1 > x:
            self.map.map_tiles[y][x + 1].put_wall(1)
        return self

    def set_east_wall_to_tile_from_to(self, x, y_from,y_to):
        for i in range(y_from,y_to+1):
            self.map.map_tiles[i][x].put_wall(3)
            if self.map.x_dim -1 > x:
                self.map.map_tiles[i][x + 1].put_wall(1)
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
        self.map.beeper_x_coord_list.append(x)
        self.map.beeper_y_coord_list.append(y)
        return self

    def unset_beeper(self,x,y):
        self.map.map_tiles[y][x].has_beeper = False
        for i in range(0, len(self.map.beeper_x_coord_list)):
            if x == self.map.beeper_x_coord_list[i] and y == self.map.beeper_y_coord_list[i]:
                del self.map.beeper_x_coord_list[i]
                del self.map.beeper_y_coord_list[i]
                break
        return self

    def set_color(self, x, y,color):
        self.map.map_tiles[y][x].color = color
        return self

    def set_token(self,x,y,value):
        self.map.map_tiles[y][x].token=Token(value)
        self.map.map_tiles[y][x].has_token = True
        self.map.token_x_coord_list.append(x)
        self.map.token_y_coord_list.append(y)
        return self

    def build(self):
        print(self.map.__str__())
        return self.map


class Token:

    def __init__(self, value):
        self.value = value
        self.picture = PhotoImage(file =token_values_pictures.get(value))


