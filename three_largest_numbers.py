import sys


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    lines = [int(line.replace('\n', '')) for line in lines]

    return lines


def calc_three_largest_number(num_list):

    max_three_num = [0] * 3 if len(num_list) >= 3 else [0] * len(num_list)

    for num in num_list:
        if num > max_three_num[0]:
            max_three_num[0] = num
            for i in range(len(max_three_num) - 1):
                if max_three_num[i] > max_three_num[i + 1]:
                    max_three_num[i], max_three_num[i + 1] = max_three_num[i + 1], max_three_num[i]

    return max_three_num[::-1]

if __name__ == '__main__':
    data = read_file(sys.argv[1])
    print calc_three_largest_number(data)
