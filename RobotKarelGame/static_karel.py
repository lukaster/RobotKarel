from RobotKarelGame.robot_karel_game import *
from RobotKarelGame.maps import *
from robot_karel.i_snek_basic import karel


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
