def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines

operators = ['*', '+']

def add(a, b):
    return a+b

def mul(a,b):
    return a*b


def part1():
    lines = get_input('short.txt')
    for l in lines:
        split_line = l.split(':')
        result = split_line[0]
        operands = list(map(int,split_line[1].split()))
        print('r: ', result, ' o:', operands)


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()