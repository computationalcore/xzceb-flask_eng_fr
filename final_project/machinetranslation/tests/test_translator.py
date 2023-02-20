"""
Test Translator module.
"""
import unittest

from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    """
    Test translator services.
    """
    def test_english_to_french(self):
        """
        Test english to french translation.
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "")

    def test_french_to_english(self):
        """
        Test french to english translation.
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "")


unittest.main()
