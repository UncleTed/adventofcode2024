import re


def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines

def part1():
    lines = get_input('long.txt')
    total = 0
    for l in lines:
        all = re.findall( "mul\(\d+,\d+\)", l)
        for a in all:
            digits = re.findall("(\d+),(\d+)", a)
            total += int(digits[0][0]) * int(digits[0][1])
    print(total)



def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()