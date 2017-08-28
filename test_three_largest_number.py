import unittest
from three_largest_numbers import calc_three_largest_number
from my_exception import FormatError


class TestThreeLargestNumber(unittest.TestCase):
    def test_three_largest_number(self):
        self.assertListEqual([6421, 8723, 9239], calc_three_largest_number('sample.dat'))

    def test_no_such_file(self):
        self.assertRaises(IOError, calc_three_largest_number, 'no_such_file.txt')

    def test_only_three_numbers(self):
        self.assertListEqual([123, 456, 999], calc_three_largest_number('only_three_number.txt'))

    def test_four_numbers(self):
        self.assertListEqual([456, 777, 999], calc_three_largest_number('four_numbers.txt'))

    def test_less_than_three_numbers(self):
        self.assertRaises(FormatError, calc_three_largest_number, 'less_than_three_numbers.txt')

    def test_empty_file(self):
        self.assertRaises(FormatError, calc_three_largest_number, 'empty.txt')

    def test_string_context_file(self):
        self.assertRaises(FormatError, calc_three_largest_number, 'string_context.txt')

if __name__ == '__main__':
    unittest.main()
