import unittest
from translator import english_to_french, french_to_english


class FrenchToEnglish(unittest.TestCase):

    def testText(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english('Comment allez-vous?'), "How are you?")
        self.assertEqual(french_to_english('Je vais bien'), "I'm fine")
        self.assertEqual(french_to_english(None), None)


class EnglishToFrench(unittest.TestCase):
    def testText(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french('How are you?'), "Comment es-tu?")
        self.assertEqual(english_to_french('I am fine'), "Je vais bien")
        self.assertEqual(english_to_french(None), None)


if __name__ == '__main__':
    unittest.main()
