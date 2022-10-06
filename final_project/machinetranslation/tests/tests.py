import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_null_english_to_french(self):
        self.assertEqual(english_to_french(''), '')


    def test_null_french_to_english(self):
        self.assertEqual(french_to_english(''), '')
        

    def test_hello_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), "Bonjour")


    def test_bonjour_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()