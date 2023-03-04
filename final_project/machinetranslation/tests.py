import unittest
from translator import  english_to_French , french_to_english

class TestMyModule1(unittest.TestCase):
    def test_english_to_French(self):
        self.assertEqual(english_to_French('Hello'), 'Bonjour')
    def test_english_to_French(self):
        self.assertNotEqual(english_to_French(0), 0)
    def test_english_to_French(self):
        self.assertNotEqual(english_to_French('None',''))

class TestMyModule2(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_french_to_english(self):    
        self.assertNotEqual(french_to_english(0), 0)
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english('None'), '')

unittest.main()

