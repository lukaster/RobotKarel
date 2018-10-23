#from RobotKarelGame import robot_karel_game
from tkinter import *
import PIL.Image
#from PIL import ImageDraw
from RobotKarelGame import maps
#import ghostscript # pip install ghostscript https://www.ghostscript.com/download.html




class PaintMap:

    def __init__(self,master,world_map):
        frame = Frame(master, highlightbackground="black", highlightcolor="black", highlightthickness=5)
        frame.pack();
        self.picture_tile = { # 0 blue, 1 green 2 purple
        0: {    0: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_no_walls.png"),
                1: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_wall_N.png"),
                2: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_wall_E.png"),
                3: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_wall_N_E.png")},
        1: {    0: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_no_walls.png"),
                1: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_wall_N.png"),
                2: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_wall_E.png"),
                3: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_wall_N_E.png")},
        2: {    0: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_no_walls.png"),
                1: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_wall_N.png"),
                2: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_wall_E.png"),
                3: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_wall_N_E.png")}
         }
        self.label_list = []
        self.master = master
        self.row_list=[]
        self.column_list = []
        for j in range(0, world_map.y_dim):
            for k in range(0, world_map.x_dim):
                tile_color = world_map.map_tiles[j][k].color
                if world_map.map_tiles[j][k].has_wall_N and world_map.map_tiles[j][k].has_wall_E:
                    self.label_list.append(
                        Label(frame, image=self.picture_tile.get(tile_color).get(3), borderwidth=0, highlightthickness=0))
                elif world_map.map_tiles[j][k].has_wall_E:
                    self.label_list.append(
                        Label(frame, image=self.picture_tile.get(tile_color).get(2), borderwidth=0, highlightthickness=0))
                elif world_map.map_tiles[j][k].has_wall_N:
                    self.label_list.append(
                        Label(frame, image=self.picture_tile.get(tile_color).get(1), borderwidth=0, highlightthickness=0))
                else:
                    self.label_list.append(
                        Label(frame, image=self.picture_tile.get(tile_color).get(0), borderwidth=0, highlightthickness=0))
                self.label_list[-1].grid(row=j, column=k)
                self.column_list.append(k)
                self.row_list.append(j)
        master.mainloop()
       # cv.postscript(file="../RobotKarelGame/eps_maps/test.eps",colormode="color")  # save canvas as encapsulated postscript
       # img = PIL.Image.open("../RobotKarelGame/eps_maps/test.eps")
       # img.save("../RobotKarelGame/maps/test.png", "png")


class PaintMapCanvas:

    def __init__(self,master,world_map):
        self.master=master
        map_width=world_map.x_dim*50
        map_height=world_map.y_dim*50
        self.canvas = Canvas(master, width=map_width, height=map_height)
        self.canvas.pack()
        self.picture_tile = { # 0 blue, 1 green 2 purple
        0: {    0: self.canvas.create_rectangle(0,0,50,50,fill = "green"),
                1: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_wall_N.png"),
                2: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_wall_E.png"),
                3: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_wall_N_E.png")},
        1: {    0: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_no_walls.png"),
                1: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_wall_N.png"),
                2: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_wall_E.png"),
                3: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_wall_N_E.png")},
        2: {    0: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_no_walls.png"),
                1: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_wall_N.png"),
                2: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_wall_E.png"),
                3: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_wall_N_E.png")}
         }
        self.label_list = []
        for j in range(0,1):
            for k in range(0, world_map.x_dim):
                tile_color = world_map.map_tiles[j][k].color
                if world_map.map_tiles[j][k].has_wall_N and world_map.map_tiles[j][k].has_wall_E:
                    self.label_list.append(
                        Label(self.canvas, image=self.picture_tile.get(tile_color).get(3), borderwidth=0, highlightthickness=0))
                elif world_map.map_tiles[j][k].has_wall_E:
                    self.label_list.append(
                        Label(self.canvas, image=self.picture_tile.get(tile_color).get(2), borderwidth=0, highlightthickness=0))
                elif world_map.map_tiles[j][k].has_wall_N:
                    self.label_list.append(
                        Label(self.canvas, image=self.picture_tile.get(tile_color).get(1), borderwidth=0, highlightthickness=0))
                else:
                    self.label_list.append(self.create_picture_tile(j*50,k*50).get(tile_color).get(0))

        self.canvas.postscript(file="../RobotKarelGame/eps_maps/test.eps",colormode="color")  # save canvas as encapsulated postscript
        img = PIL.Image.open("../RobotKarelGame/eps_maps/test.eps")
        img.save("../RobotKarelGame/maps/test.png", "png")
        master.mainloop()

    def create_picture_tile(self,x,y):
        return {  # 0 blue, 1 green 2 purple
            0: {0: self.canvas.create_rectangle(x, y, x+50, y+50, fill="#A0CFE0"),
                1: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_wall_N.png"),
                2: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_wall_E.png"),
                3: PhotoImage(file="../RobotKarelGame/pictures/tiles/tile_wall_N_E.png")},
            1: {0: self.canvas.create_rectangle(x, y, x+50, y+50, fill="#5CEB8B"),
                1: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_wall_N.png"),
                2: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_wall_E.png"),
                3: PhotoImage(file="../RobotKarelGame/pictures/tiles/green/tile_wall_N_E.png")},
            2: {0: self.canvas.create_rectangle(x, y, x+50, y+50, fill="#C57EEB"),
                1: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_wall_N.png"),
                2: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_wall_E.png"),
                3: PhotoImage(file="../RobotKarelGame/pictures/tiles/purple/tile_wall_N_E.png")}
        }



root = Tk()
world_map = maps.map_test_token(root)
PaintMap(root,world_map)