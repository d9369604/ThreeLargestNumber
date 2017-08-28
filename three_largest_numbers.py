import sys
import os
from my_exception import FormatError


def check_data_format(context):
    if not all([line.replace('\n', '').isdigit() for line in context]):
        raise FormatError('content format is wrong')


def read_file(filename):
    with open(os.path.join(os.getcwd(), 'input', filename)) as f:
        lines = f.readlines()

    check_data_format(lines)
    lines = [int(line.replace('\n', '')) for line in lines]

    if len(lines) < 3:
        raise FormatError('Number of numbers is less than 3')

    return lines


def calc_three_largest_number(filename):

    num_list = read_file(filename)

    max_three_num = [0] * 3

    for num in num_list:
        if num > max_three_num[0]:
            max_three_num[0] = num
            for i in range(2):
                if max_three_num[i] > max_three_num[i + 1]:
                    max_three_num[i], max_three_num[i + 1] = max_three_num[i + 1], max_three_num[i]

    return max_three_num

if __name__ == '__main__':
    print calc_three_largest_number(sys.argv[1])
