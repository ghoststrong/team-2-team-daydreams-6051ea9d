from unittest import TestCase
from levelup.position import Position

class TestPosition(TestCase):
    def test_init(self):
        COORDINATES = ("3","4")
        testobj = Position(COORDINATES)
        self.assertEqual(COORDINATES, testobj.coordinates)

class TestInsanePosition(TestCase):
    def test_init(self):
        COORDINATES = ("10","22")
        testobj = Position(COORDINATES)
        self.assertEqual(COORDINATES, testobj.coordinates)
