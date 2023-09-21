from unittest import TestCase
from levelup.map import GameMap
#from levelup.position import Position

class TestGameMapPositionCount(TestCase):
    def test_init(self):
        EXPECTED_NUMPOSITIONS = 100
        testobj = GameMap()
        self.assertEqual(EXPECTED_NUMPOSITIONS, testobj.numPositions)
'''
class TestGameMapGetPositions(TestCase):
    def test_init(self):
        EXPECTED_NUMPOSITIONS = 100
        testobj = GameMap()
        position_results[] = testobj.getPositions()
        total_positions = len(position_results)
        position_set = set(total_positions)
        unique_count = len(positions_set)
        self.assertEqual(EXPECTED_NUMPOSITIONS, total_positions)
        self.assertEqual(EXPECTED_NUMPOSITIONS, unique_count)

        for position in position_results:
            if (position[0] in range(0, 9)) AND (position[1] in range(0,9) AND  )



class TestGameMap(TestCase):
    def test_init(self):
        testobj = GameMap()
'''

