from unittest import TestCase
from levelup.gamestatus import GameStatus

class TestGameStatus(TestCase):
    def test_init(self):
        CHARACTER_NAME = "Matt"
        COORDINATES = ("5","9")
        MOVE_COUNT = 24

        testobj = GameStatus(CHARACTER_NAME, COORDINATES, MOVE_COUNT)
      
        print(testobj.toString())
        self.assertEqual("(24) Matt is currently at position [5,9]", 
            testobj.toString())