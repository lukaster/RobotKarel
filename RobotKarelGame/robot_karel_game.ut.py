import unittest
from RobotKarelGame import robot_karel_game

class TestGame(unittest.TestCase):
    def setUp(self):
        karel = robot_karel_game.RobotKarel(1,1)
        m = robot_karel_game.WorldMap(3,3,karel)
        print(m.__str__())
        self.func = robot_karel_game.Game(m)

    def test_move(self):
        print("----test move ----")
        """karel obejde counterclockwise kolo, kontrola coord a direction"""
        self.assertTrue(self.func.karel.x == 1)
        self.assertTrue(self.func.karel.y == 1)
        self.assertTrue(self.func.karel.facing_directionInt == 0)

        self.func.move()
        self.assertTrue(self.func.karel.x == 1)
        self.assertTrue(self.func.karel.y == 0)
        self.assertTrue(self.func.karel.facing_directionInt == 0)

        self.func.turn_left()
        self.func.move()
        self.assertTrue(self.func.karel.x == 0)
        self.assertTrue(self.func.karel.y == 0)
        self.assertTrue(self.func.karel.facing_directionInt == 1)

        self.func.turn_left()
        self.func.move()
        self.assertTrue(self.func.karel.x == 0)
        self.assertTrue(self.func.karel.y == 1)
        self.assertTrue(self.func.karel.facing_directionInt == 2)

        self.func.turn_left()
        self.func.move()
        self.assertTrue(self.func.karel.x == 1)
        self.assertTrue(self.func.karel.y == 1)
        self.assertTrue(self.func.karel.facing_directionInt == 3)

        self.func.turn_left()
        self.assertTrue(self.func.karel.x == 1)
        self.assertTrue(self.func.karel.y == 1)
        self.assertTrue(self.func.karel.facing_directionInt == 0)

    def test_turn_left(self):
        print("---test turn left---")
        """karel se otoci, kontrola direction"""
        self.assertTrue(self.func.karel.facing_directionInt == 0)
        self.func.turn_left()
        self.assertTrue(self.func.karel.facing_directionInt == 1)
        self.func.turn_left()
        self.assertTrue(self.func.karel.facing_directionInt == 2)
        self.func.turn_left()
        self.assertTrue(self.func.karel.facing_directionInt == 3)
        self.func.turn_left()
        self.assertTrue(self.func.karel.facing_directionInt == 0)
        print("turn left tested")

    def test_is_on_beeper(self):
        """pred robotem beeper, udela krok a je hodnota true"""
        print("---test is on beeper ---")
        self.func.map = robot_karel_game.MapBuilder(self.func.map).set_beeper(1,0).build()
        self.assertFalse(self.func.is_on_beeper())
        self.func.move()
        self.assertTrue(self.func.is_on_beeper())

    def test_pick_up_and_put_down_beeper(self):
        """pred robotem beeper, udela krok a beeper sebere, otoci se doleva, poponese krok, polozi, otoci se a popojde"""
        print("---test pick up beeper ---")
        self.func.map = robot_karel_game.MapBuilder(self.func.map).set_beeper(1,0).build()
        self.assertFalse(self.func.is_on_beeper())
        self.func.move()
        self.assertTrue(self.func.is_on_beeper())
        self.func.pick_up_beeper()
        self.assertFalse(self.func.is_on_beeper())
        self.assertTrue(self.func.karel.has_beeper)
        self.func.turn_left()
        self.func.move()
        self.func.put_down_beeper()
        self.assertFalse(self.func.karel.has_beeper)
        self.assertTrue(self.func.is_on_beeper())
        self.func.turn_left()
        self.func.move()


    def test_walls(self):
        print("---test walls---")
        """robot uvnitr zdi, kontrola tvorby zdi v builderu a pak ze v kazdem smeru robot neprojde a jeho souradnice zustanou"""
        self.func.map = robot_karel_game.MapBuilder(self.func.map)\
            .set_east_wall_to_tile(1,1)\
            .set_north_wall_to_tile(1,1)\
            .set_west_wall_to_tile(1,1)\
            .set_south_wall_to_tile(1,1)\
            .build()

        self.assertTrue(self.func.map.map_tiles[0][1].has_wall_S)
        self.assertTrue(self.func.map.map_tiles[1][1].has_wall_S)
        self.assertTrue(self.func.map.map_tiles[1][2].has_wall_W)
        self.assertTrue(self.func.map.map_tiles[1][1].has_wall_E)
        self.assertTrue(self.func.map.map_tiles[2][1].has_wall_N)
        self.assertTrue(self.func.map.map_tiles[1][1].has_wall_N)
        self.assertTrue(self.func.map.map_tiles[1][0].has_wall_E)
        self.assertTrue(self.func.map.map_tiles[1][1].has_wall_W)

        self.func.move()
        self.assertTrue(self.func.karel.x == 1)
        self.assertTrue(self.func.karel.y == 1)

        self.func.turn_left()
        self.func.move()
        self.assertTrue(self.func.karel.x == 1)
        self.assertTrue(self.func.karel.y == 1)

        self.func.turn_left()
        self.func.move()
        self.assertTrue(self.func.karel.x == 1)
        self.assertTrue(self.func.karel.y == 1)

        self.func.turn_left()
        self.func.move()
        self.assertTrue(self.func.karel.x == 1)
        self.assertTrue(self.func.karel.y == 1)

    def test_is_in_front_of_the_wall(self):
        print("---test is in front of the wall ---")
        print("--testing edges--")
        """konec mapy se pocita jako zed v logice, proto ma byt true"""
        self.func.move()
        self.assertTrue(self.func.is_in_front_of_the_wall() == True)
        self.func.turn_left()
        self.func.move()
        self.assertTrue(self.func.is_in_front_of_the_wall() == True)

        self.func.turn_left()
        self.func.move()
        self.func.move()
        self.assertTrue(self.func.is_in_front_of_the_wall() == True)

        self.func.turn_left()
        self.func.move()
        self.func.move()
        self.assertTrue(self.func.is_in_front_of_the_wall() == True)

        print("--testin walls--")
        """pokud je pred zdi ma vratit true"""
        self.func.map = robot_karel_game.MapBuilder(self.func.map) \
            .set_robot(1,1)\
            .set_east_wall_to_tile(1, 1) \
            .set_north_wall_to_tile(1, 1) \
            .set_west_wall_to_tile(1, 1) \
            .set_south_wall_to_tile(1, 1) \
            .build()
        self.func.karel.set_coord(1,1)
        self.assertTrue(self.func.is_in_front_of_the_wall() == True)
        self.func.turn_left()
        self.assertTrue(self.func.is_in_front_of_the_wall() == True)
        self.func.turn_left()
        self.assertTrue(self.func.is_in_front_of_the_wall() == True)
        self.func.turn_left()
        self.assertTrue(self.func.is_in_front_of_the_wall() == True)
        print("------------")
if __name__ == '__main__':
    unittest.main()
