import sys


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [int(line.replace('\n', '')) for line in lines]
    return lines


def three_largest_number(filename):

    num_list = read_file(filename)

    max_three_num = [0] * 3

    for num in num_list:
        if num > max_three_num[0]:
            max_three_num[0] = num
            for i in range(2):
                if max_three_num[i] > max_three_num[i + 1]:
                    max_three_num[i], max_three_num[i + 1] = max_three_num[i + 1], max_three_num[i]

    for i in range(2, -1, -1):
        print(max_three_num[i])

if __name__ == '__main__':
    three_largest_number(sys.argv[1])
