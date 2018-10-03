from RobotKarelGame import robot_karel_game
from tkinter import *

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
        .build()
    return m

def map_bot_corner(master):
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
        .build()
    return m

def map_maze(master):
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
        .set_beeper(1, 5) \
        .build()
    return m
