from validations import *
import unittest

class TestValidations (unittest.TestCase):
    def test_dataTypeCheck_word_true_word (self):
        a,b = dataTypeCheck("word_characters", "aZa")
        self.assertEqual(a, True)
        self.assertEqual(b, "word_characters")

    def test_dataTypeCheck_word_false_digit (self):
        a,b = dataTypeCheck("word_characters", "134")
        self.assertEqual(a, False)
        self.assertEqual(b, "digits")

    def test_dataTypeCheck_word_false_other (self):
        a,b = dataTypeCheck("word_characters", "aR#$")
        self.assertEqual(a, False)
        self.assertEqual(b, "")

    def test_dataTypeCheck_digit_true_digit (self):
        a,b = dataTypeCheck("digits", "123")
        self.assertEqual(a, True)
        self.assertEqual(b, "digits")

    def test_dataTypeCheck_digit_false_word (self):
        a,b = dataTypeCheck("digits", "abscd")
        self.assertEqual(a, False)
        self.assertEqual(b, "word_characters")

    def test_dataTypeCheck_digit_false_other (self):
        a,b = dataTypeCheck("digits", "123.#")
        self.assertEqual(a, False)
        self.assertEqual(b, "")

    def test_maxLengthCheck_True (self):
        a = maxLengthCheck(3, "aZa")
        self.assertEqual(a, True)

    def test_maxLengthCheck_False (self):
        a = maxLengthCheck(2, "aZa")
        self.assertEqual(a, False)
        
    def test_findErrorCode_1 (self):
        a = findErrorCode(True, True)
        self.assertEqual(a, 'E01')
    
    def test_findErrorCode_2 (self):
        a = findErrorCode(False, True)
        self.assertEqual(a, 'E02')

    def test_findErrorCode_3 (self):
        a = findErrorCode(True, False)
        self.assertEqual(a, 'E03')

    def test_findErrorCode_4 (self):
        a = findErrorCode(False, False)
        self.assertEqual(a, 'E04')

if __name__=='__main__':
    unittest.main()