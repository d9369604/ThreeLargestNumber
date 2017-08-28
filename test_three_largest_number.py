import unittest
from three_largest_numbers import calc_three_largest_number


class TestThreeLargestNumber(unittest.TestCase):
    def test_normal_case(self):
        test_data = [2134, 3412, 6421, 8723, 9239, 1234, 2345]
        self.assertEqual([9239, 8723, 6421], calc_three_largest_number(test_data))

    def test_no_number(self):
        self.assertEqual([], calc_three_largest_number([]))

    def test_one_number(self):
        self.assertEqual([777], calc_three_largest_number([777]))

    def test_only_three_numbers(self):
        self.assertEqual([999, 456, 123], calc_three_largest_number([999, 123, 456]))

    def test_four_numbers(self):
        self.assertEqual([999, 777, 456], calc_three_largest_number([999, 123, 456, 777]))

    def test_many_numbers(self):
        test_data = [111, 234, 173, 999, 34324, 90573, 85928, 1, 0,
                     396849, 8374729, 7727349, 1194545, 338483, 10,
                     993834, 23212340, 9459230, 94572, 4545, 234254]
        self.assertEqual([23212340, 9459230, 8374729], calc_three_largest_number(test_data))

if __name__ == '__main__':
    unittest.main()
