from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    def test_init(self):
        COORDINATES = (3,4)
        testobj = Position(COORDINATES)
        self.assertEqual(COORDINATES, testobj.coordinates)
        self.assertEqual(testobj.get_x_coord(), 3)
        self.assertEqual(testobj.get_y_coord(), 4)

class TestInsanePosition(TestCase):
    def test_init(self):
        COORDINATES = ("10","22")
        testobj = Position(COORDINATES)
        self.assertEqual(COORDINATES, testobj.coordinates)
