#Christine Mier
#November 19, 2024
#This program runs and tests unittests for the file 'StringCalculator.py'

import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    '''Tests the string calculator file'''
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calc.add(''), 0)

    def test_single_number(self):
        self.assertEqual(self.calc.add('5'), 5)

    def test_two_numbers(self):
        self.assertEqual(self.calc.add('3,7'), 10)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.add('1,2,3,4,5'), 15)

    def test_add_newline(self):
        self.assertEqual(self.calc.add('1\n2,3'), 6)

    def test_ignore_larger_than_1000(self):
        self.assertEqual(self.calc.add('1001, 2,3'), 3)

    def test_multiple_same_delimiters(self):
        self.assertEqual(self.calc.add('1,1,1'), 3)

    def test_multiple_delimiters(self):
        self.assertEqual(self.calc.add('1,2,3'), 6)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.calc.add('1,-2,3')

    def test_custom_delimiter(self):
        self.assertEqual(self.calc.add('//[*]\n1*9'), 10)

    def test_multiple_custom_delimiters(self):
        self.assertEqual(self.calc.add('//[;][*]\n1;2%3'), 0)

    def test_custom_delimiter_with_multiple_characters(self):
        self.assertEqual(self.calc.add('//[***][%]\n1***2%3'), 0)

    def test_custom_delimiter_with_newline(self):
        self.assertEqual(self.calc.add('//[;;]\n1;;2;;3'), 6)

    def test_large_numbers_with_negative(self):
        with self.assertRaises(ValueError):
            self.calc.add('1,-1001,2')

    def test_newline_and_comma(self):
        self.assertEqual(self.calc.add('1\n2,3,4\n5'), 15)

if __name__ == '__main__':
    unittest.main()
