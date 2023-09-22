from unittest import TestCase
from levelup.character import Character
from fake_map import FakeMap


class TestCharacter(TestCase):
    ARBITRARY_NAME = "Ryan"
    
    def test_initialize(self):
        testobject = Character(self.ARBITRARY_NAME)
        self.assertEqual(self.ARBITRARY_NAME, testobject.name)

    def test_entermap(self):
        testobject = Character(self.ARBITRARY_NAME)
        fakemap = FakeMap()
        testobject.enter_map(fakemap)
        self.assertEqual(testobject.current_position, fakemap.starting_position)


