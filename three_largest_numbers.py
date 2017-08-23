import sys


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [int(line.replace('\n', '')) for line in lines]
    return lines


def three_largest_number(filename):
    nums = read_file(filename)
    for i in range(3):
        max_num = max(nums)
        print(max_num)
        nums.remove(max_num)


if __name__ == '__main__':
    three_largest_number(sys.argv[1])
