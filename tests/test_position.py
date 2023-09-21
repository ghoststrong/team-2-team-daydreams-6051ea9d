from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    def test_init(self):
        COORDINATES = ("3","4")
        testobj = Position(COORDINATES)
        print(testobj.coordinates)
        self.assertEqual(COORDINATES, testobj.coordinates)