from RobotKarelGame import robot_karel_game
from tkinter import *

def map1(master):
    karel = robot_karel_game.RobotKarel(4, 1,master)
    m = robot_karel_game.WorldMap(6, 6, karel,master)
    m.background_image = PhotoImage(file="../robot_karel/map1.png")
    m = robot_karel_game.MapBuilder(m)\
        .set_east_wall_to_tile(1,0)\
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
        .set_beeper(2, 5) \
        .build()
    return m

