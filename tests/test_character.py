from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)


class TestCharacterGetName(TestCase):
    def test_init(self):
        TEST_NAME = "Ryan"
        testobj = Character(TEST_NAME)
        result = testobj.getName()
        self.assertEqual(TEST_NAME, result)
