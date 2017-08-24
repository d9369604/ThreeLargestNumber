import sys


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [int(line.replace('\n', '')) for line in lines]
    return lines


def three_largest_number(filename):

    num_list = read_file(filename)

    max_three_num = []
    cur_max_num = 0

    for i in range(3):
        for num in num_list:
            if num > cur_max_num and num not in max_three_num:
                cur_max_num = num
        max_three_num += [cur_max_num]
        cur_max_num = 0

    for num in max_three_num:
        print(num)

if __name__ == '__main__':
    three_largest_number(sys.argv[1])
