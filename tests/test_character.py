from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestCharacterInitWithEmptyName(TestCase):
    def test_init(self):
        EMPTY_NAME = ""
        EXPECTED_NAME = "Character"
        testobj = Character(EMPTY_NAME)
        self.assertEqual(EXPECTED_NAME, testobj.name)
