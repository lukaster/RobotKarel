from RobotKarelGame import robot_karel_game
from tkinter import *
import random

def map1(master):
    karel = robot_karel_game.RobotKarel(0, 3)
    m = robot_karel_game.WorldMap(6, 6, karel,master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map1.png")
    m = robot_karel_game.MapBuilder(m)\
        .set_east_wall_to_tile(1, 0)\
        .set_south_wall_to_tile(1, 0)\
        .set_east_wall_to_tile(0, 1)\
        .set_south_wall_to_tile(0, 1) \
        .set_west_wall_to_tile(4, 0) \
        .set_south_wall_to_tile(4, 0) \
        .set_west_wall_to_tile(5, 1) \
        .set_south_wall_to_tile(5, 1) \
        .set_north_wall_to_tile(0, 4) \
        .set_east_wall_to_tile(0, 4) \
        .set_north_wall_to_tile(1, 5) \
        .set_east_wall_to_tile(1, 5) \
        .set_north_wall_to_tile(4, 5) \
        .set_west_wall_to_tile(4, 5) \
        .set_north_wall_to_tile(5, 4) \
        .set_west_wall_to_tile(5, 4) \
        .set_beeper(3, 0) \
        .set_beeper(3, 5) \
        .set_color(5, 2, 2) \
        .set_color(5, 3, 1) \
        .build()
    return m

def map_test_token(master):
    karel = robot_karel_game.RobotKarel(0, 0)
    karel.facing_directionInt = 3
    m = robot_karel_game.WorldMap(11, 1, karel, master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map_test_token_sort.png")
    m = robot_karel_game.MapBuilder(m) \
        .set_color(0,0,1) \
        .set_token(7,0,7) \
        .set_token(5, 0, 1) \
        .set_token(1, 0, 2) \
        .set_token(2, 0, 3) \
        .set_token(3, 0, 0) \
        .set_token(4, 0, 4) \
        .set_token(10, 0, 8) \
        .set_token(6, 0, 9) \
        .set_token(8, 0, 6) \
        .set_token(9, 0, 5) \
        .build()
    return m

def map_loop_move_b(master):
    karel = robot_karel_game.RobotKarel(0, 0)
    karel.facing_directionInt=3
    m = robot_karel_game.WorldMap(19, 1, karel,master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/noodle.png")
    m = robot_karel_game.MapBuilder(m)\
        .set_beeper(1, 0) \
        .set_beeper(3, 0) \
        .set_beeper(5, 0) \
        .set_beeper(7, 0) \
        .set_beeper(9, 0) \
        .set_beeper(11, 0) \
        .set_beeper(13, 0) \
        .set_beeper(15, 0) \
        .set_beeper(17, 0) \
        .build()
    return m

def map_loop_move_b_color_1(master):
    karel = robot_karel_game.RobotKarel(0, 0)
    karel.facing_directionInt=3
    m = robot_karel_game.WorldMap(19, 1, karel,master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/noodle_red.png")
    m = robot_karel_game.MapBuilder(m)\
        .set_beeper(1, 0) \
        .set_beeper(3, 0) \
        .set_beeper(5, 0) \
        .set_beeper(7, 0) \
        .set_beeper(9, 0) \
        .set_beeper(11, 0) \
        .set_beeper(13, 0) \
        .set_beeper(15, 0) \
        .set_beeper(17, 0) \
        .set_color(3,0,2) \
        .set_color(5, 0, 2) \
        .set_color(9, 0, 2) \
        .set_color(17, 0, 2) \
        .build()
    return m


def map_loop_move_b_color_2(master):
    karel = robot_karel_game.RobotKarel(0, 0)
    karel.facing_directionInt=3
    m = robot_karel_game.WorldMap(19, 1, karel,master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/noodle_red_green.png")
    m = robot_karel_game.MapBuilder(m)\
        .set_beeper(1, 0) \
        .set_beeper(3, 0) \
        .set_beeper(5, 0) \
        .set_beeper(7, 0) \
        .set_beeper(9, 0) \
        .set_beeper(11, 0) \
        .set_beeper(13, 0) \
        .set_beeper(15, 0) \
        .set_beeper(17, 0) \
        .set_color(3,0,2) \
        .set_color(5, 0, 2) \
        .set_color(9, 0, 2) \
        .set_color(17, 0, 2) \
        .set_color(4, 0, 1) \
        .set_color(8, 0, 1) \
        .set_color(14, 0, 1) \
        .set_color(18, 0, 1) \
        .build()
    return m

def map_loop_snek(master):
    karel = robot_karel_game.RobotKarel(0, 1)
    m = robot_karel_game.WorldMap(19, 2, karel,master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map_snek_basic.png")
    m = robot_karel_game.MapBuilder(m) \
        .set_east_wall_to_tile(0, 1) \
        .set_east_wall_to_tile(1, 0)\
         .set_east_wall_to_tile(2, 1) \
        .set_east_wall_to_tile(3, 0) \
        .set_east_wall_to_tile(4, 1) \
        .set_east_wall_to_tile(5, 0) \
        .set_east_wall_to_tile(6, 1) \
        .set_east_wall_to_tile(7, 0) \
        .set_east_wall_to_tile(8, 1) \
        .set_east_wall_to_tile(9, 0) \
        .set_east_wall_to_tile(10, 1) \
        .set_east_wall_to_tile(11, 0) \
        .set_east_wall_to_tile(12, 1) \
        .set_east_wall_to_tile(13, 0) \
        .set_east_wall_to_tile(14, 1) \
        .set_east_wall_to_tile(15, 0) \
        .set_east_wall_to_tile(16, 1) \
        .set_east_wall_to_tile(17, 0) \
        .set_east_wall_to_tile(18, 1) \
        .build()
    return m

def map_loop_snek_green(master):
    m = map_loop_snek(master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map_snek_green.png")
    m = robot_karel_game.MapBuilder(m) \
        .set_color(3,0,1) \
        .set_color(8, 0, 1) \
        .set_color(10, 1, 1) \
        .set_color(15, 1, 1) \
        .set_color(3, 0, 1) \
        .set_beeper(0,0) \
        .set_beeper(5, 1) \
        .set_beeper(9, 0) \
        .set_beeper(12, 0) \
        .build()
    return m

def map_loop_snek_green_red(master):
    m=map_loop_snek_green(master);
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map_snek_green_red.png")
    m = robot_karel_game.MapBuilder(m) \
        .set_color(1,1,2) \
        .set_color(2, 1, 2) \
        .set_color(0, 1, 2) \
        .set_color(1, 0, 2) \
        .build()
    return m

def map_green_square(master):
    karel = robot_karel_game.RobotKarel(6, 4)
    m = robot_karel_game.WorldMap(8, 8, karel, master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map_green_square.png")
    m = robot_karel_game.MapBuilder(m) \
        .set_color(6,5,1) \
        .set_color(6, 1, 1) \
        .set_color(1, 1, 1) \
        .set_color(1, 5, 1) \
        .build()
    return m

def map_green_and_red_lap(master):
    karel = robot_karel_game.RobotKarel(10, 9)
    m = robot_karel_game.WorldMap(12, 12, karel, master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map_green_and_red_lap.png")
    m = robot_karel_game.MapBuilder(m) \
        .set_color(10,8,1) \
        .set_color(7, 8, 2) \
        .set_color(7, 4, 2) \
        .set_color(9, 4, 1) \
        .set_color(9, 0, 1) \
        .set_color(1, 0, 1) \
        .set_color(1, 4, 1) \
        .set_color(1, 0, 1) \
        .set_color(3, 8, 1) \
        .set_color(3, 11, 1) \
        .set_color(10, 11, 1) \
        .build()
    return m

def map_bot_corner(master):
    x = random.randint(0, 11)
    y = random.randint(0, 7)
    karel = robot_karel_game.RobotKarel(9, 1)
    m = robot_karel_game.WorldMap(12, 8, karel,master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map_bot_corner.png")
    m = robot_karel_game.MapBuilder(m)\
        .set_south_wall_to_tiles_from_to(5, 11, 4)\
        .set_south_wall_to_tile(0, 2) \
        .set_south_wall_to_tile(0, 4) \
        .set_east_wall_to_tile_from_to(0, 3, 4) \
        .set_east_wall_to_tile_from_to(4, 5, 7) \
        .set_beeper(11, 1) \
        .set_beeper(11, 3) \
        .set_beeper(7, 4) \
        .set_beeper(4, 5) \
        .set_beeper(3, 7) \
        .set_beeper(1, 7) \
        .set_beeper(1, 3) \
        .set_beeper(0, 1) \
        .set_beeper(3, 0) \
        .set_beeper(5, 0) \
        .set_beeper(6, 0) \
        .set_beeper(7, 0) \
        .set_color(x,y,2)\
        .build()
    return m

def map_maze(master):
    x_beeper = random.randint(0,9)
    y_beeper = random.randint(0, 9)
    x_green = random.randint(0,9)
    y_green = random.randint(0,9)
    karel = robot_karel_game.RobotKarel(1, 1)
    m = robot_karel_game.WorldMap(10, 10, karel,master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/maze.png")
    m = robot_karel_game.MapBuilder(m)\
        .set_south_wall_to_tile(1, 0) \
        .set_south_wall_to_tile(4, 0) \
        .set_south_wall_to_tile(6, 0) \
        .set_south_wall_to_tile(1, 1) \
        .set_south_wall_to_tile(2, 1) \
        .set_south_wall_to_tile(3, 1) \
        .set_south_wall_to_tile(5, 1) \
        .set_south_wall_to_tile(6, 1) \
        .set_south_wall_to_tile(8, 1) \
        .set_south_wall_to_tile(0, 2) \
        .set_south_wall_to_tile(1, 2) \
        .set_south_wall_to_tile(6, 2) \
        .set_south_wall_to_tile(7, 2) \
        .set_south_wall_to_tile(9, 2) \
        .set_south_wall_to_tile(2, 3) \
        .set_south_wall_to_tile(4, 3) \
        .set_south_wall_to_tile(5, 3) \
        .set_south_wall_to_tile(6, 3) \
        .set_south_wall_to_tile(7, 3) \
        .set_south_wall_to_tile(0, 4) \
        .set_south_wall_to_tile(1, 4) \
        .set_south_wall_to_tile(3, 4) \
        .set_south_wall_to_tile(5, 4) \
        .set_south_wall_to_tile(6, 4) \
        .set_south_wall_to_tile(8, 4) \
        .set_south_wall_to_tile(2, 5) \
        .set_south_wall_to_tile(4, 5) \
        .set_south_wall_to_tile(7, 5) \
        .set_south_wall_to_tile(1, 6) \
        .set_south_wall_to_tile(2, 6) \
        .set_south_wall_to_tile(3, 6) \
        .set_south_wall_to_tile(5, 6) \
        .set_south_wall_to_tile(6, 6) \
        .set_south_wall_to_tile(8, 6) \
        .set_south_wall_to_tile(9, 6) \
        .set_south_wall_to_tile(0, 7) \
        .set_south_wall_to_tile(3, 7) \
        .set_south_wall_to_tile(4, 7) \
        .set_south_wall_to_tile(5, 7) \
        .set_south_wall_to_tile(7, 7) \
        .set_south_wall_to_tile(8, 7) \
        .set_south_wall_to_tile(1, 8) \
        .set_south_wall_to_tile(3, 8) \
        .set_south_wall_to_tile(8, 8) \
        .set_east_wall_to_tile(0, 1) \
        .set_east_wall_to_tile(0, 3) \
        .set_east_wall_to_tile(0, 6) \
        .set_east_wall_to_tile(1, 4) \
        .set_east_wall_to_tile(1, 5) \
        .set_east_wall_to_tile(1, 7) \
        .set_east_wall_to_tile(1, 8) \
        .set_east_wall_to_tile(2, 0) \
        .set_east_wall_to_tile(2, 1) \
        .set_east_wall_to_tile(2, 3) \
        .set_east_wall_to_tile(3, 0) \
        .set_east_wall_to_tile(3, 3) \
        .set_east_wall_to_tile(3, 5) \
        .set_east_wall_to_tile(3, 6) \
        .set_east_wall_to_tile(3, 8) \
        .set_east_wall_to_tile(4, 1) \
        .set_east_wall_to_tile(4, 2) \
        .set_east_wall_to_tile(4, 3) \
        .set_east_wall_to_tile(4, 4) \
        .set_east_wall_to_tile(4, 6) \
        .set_east_wall_to_tile(4, 7) \
        .set_east_wall_to_tile(4, 9) \
        .set_east_wall_to_tile(5, 0) \
        .set_east_wall_to_tile(5, 5) \
        .set_east_wall_to_tile(5, 8) \
        .set_east_wall_to_tile(6, 6) \
        .set_east_wall_to_tile(6, 7) \
        .set_east_wall_to_tile(6, 9) \
        .set_east_wall_to_tile(7, 0) \
        .set_east_wall_to_tile(7, 1) \
        .set_east_wall_to_tile(7, 2) \
        .set_east_wall_to_tile(7, 4) \
        .set_east_wall_to_tile(7, 5) \
        .set_east_wall_to_tile(8, 1) \
        .set_east_wall_to_tile(8, 3) \
        .set_east_wall_to_tile(8, 5) \
        .set_east_wall_to_tile(8, 8) \
        .set_beeper(x_beeper, y_beeper) \
        .set_color(x_green,y_green,1)\
        .build()
    return m


def map_loop_basic(master):
    karel = robot_karel_game.RobotKarel(0, 0)
    m = robot_karel_game.WorldMap(9, 9, karel,master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map_loop_basic.png")
    m = robot_karel_game.MapBuilder(m)\
        .set_south_wall_to_tiles_from_to(1, 7, 7)\
        .set_east_wall_to_tile_from_to(0, 1, 7) \
        .set_east_wall_to_tile_from_to(7, 1, 7) \
        .set_south_wall_to_tile(1,0) \
        .set_south_wall_to_tile(3, 0) \
        .set_south_wall_to_tile(5, 0) \
        .set_south_wall_to_tile(7, 0) \
        .set_south_wall_to_tile(2, 1) \
        .set_south_wall_to_tile(4, 1) \
        .set_south_wall_to_tile(6, 1) \
        .set_east_wall_to_tile(6,1) \
        .set_east_wall_to_tile(1, 1) \
        .set_east_wall_to_tile(2, 1) \
        .set_east_wall_to_tile(3, 1) \
        .set_east_wall_to_tile(4, 1) \
        .set_east_wall_to_tile(5, 1) \
        .set_color(2,0,2) \
        .set_color(4, 0, 2) \
        .set_color(6, 0, 2) \
        .set_color(2, 1, 1) \
        .set_color(4, 1, 1) \
        .set_color(6, 1, 1) \
        .set_beeper(0, 2) \
        .set_beeper(5, 8) \
        .set_beeper(8, 4) \
        .build()
    return m

def map_loop_tokens(master):
    m = map_loop_basic(master)
    m = robot_karel_game.MapBuilder(m)\
        .unset_beeper(0, 2) \
        .unset_beeper(5, 8) \
        .unset_beeper(8, 4) \
        .set_token(0, 2,0) \
        .set_token(5, 8,1) \
        .set_token(8, 4,2) \
        .build()
    return m

def map_loop_tokens_odd_even(master):
    m = map_loop_basic(master)
    m = robot_karel_game.MapBuilder(m)\
        .unset_beeper(0, 2) \
        .unset_beeper(5, 8) \
        .unset_beeper(8, 4) \
        .set_token(0, 2,1) \
        .set_token(5, 8,7) \
        .set_token(8, 4,5) \
        .set_token(0, 6, 4) \
        .set_token(1, 8, 8) \
        .set_token(8, 1, 2) \
        .build()
    return m

def map_wide_green(master):
    karel = robot_karel_game.RobotKarel(0, 8)
    m = robot_karel_game.WorldMap(9, 9, karel,master)
    m.background_image = PhotoImage(file="../RobotKarelGame/maps/map_wide_green.png")
    m = robot_karel_game.MapBuilder(m)\
        .set_color(2,1,1) \
        .set_color(4, 1, 1) \
        .set_color(6, 1, 1) \
        .set_color(2, 3, 1) \
        .set_color(4, 3, 1) \
        .set_color(6, 3, 1) \
        .set_beeper(3, 8) \
        .set_beeper(4, 8) \
        .set_beeper(5, 8) \
        .set_beeper(6, 8) \
        .set_beeper(7, 8) \
        .set_beeper(8, 8) \
        .build()
    return m



class PaintMap:

    def __init__(self,master,world_map):
        self.frame = Frame(master, highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame.pack();
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
                        Label(self.frame, image=self.picture_tile.get(tile_color).get(3), borderwidth=0, highlightthickness=0))
                elif world_map.map_tiles[j][k].has_wall_E:
                    self.label_list.append(
                        Label(self.frame, image=self.picture_tile.get(tile_color).get(2), borderwidth=0, highlightthickness=0))
                elif world_map.map_tiles[j][k].has_wall_N:
                    self.label_list.append(
                        Label(self.frame, image=self.picture_tile.get(tile_color).get(1), borderwidth=0, highlightthickness=0))
                else:
                    self.label_list.append(
                        Label(self.frame, image=self.picture_tile.get(tile_color).get(0), borderwidth=0, highlightthickness=0))
                self.column_list.append(k)
                self.row_list.append(j)



