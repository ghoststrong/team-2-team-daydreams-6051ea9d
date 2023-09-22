from unittest import TestCase
from levelup.character import Character


class TestCharacter(TestCase):
    ARBITRARY_NAME = "Ryan"
    
    def test_initialize(self):
        testobject = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobject.name)




