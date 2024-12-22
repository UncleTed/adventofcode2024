import re


def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines

def part1():
    lines = get_input('long.txt')
    total = 0
    for l in lines:
        all = re.findall( r"mul\((\d+),(\d+)\)", l)
        for a in all:
            d1,d2 = map(int, a)
            total += d1 * d2
    print(total)



def part2():
    lines = get_input('long.txt')
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    mul_pattern = r"mul\((\d+),(\d+)\)"
    for l in lines:
        mul = re.finditer( mul_pattern, l)
        do = re.finditer(do_pattern, l)
        dont = re.finditer(dont_pattern, l)

    all = list(mul) + list(do) + list(dont)
    regexes = sorted(all, key=lambda x: x.start())

    total = 0
    on = True
    for r in regexes:    
        if r.re.pattern == mul_pattern:
            if on:
                d1,d2 = map(int, r.groups())
                total += d1 * d2
                print(total)
        elif r.re.pattern == do_pattern:
            print("DO")
            on = True
        elif r.re.pattern == dont_pattern:
            print("NOT")
            on = False
    print(total)


if __name__ == "__main__":
    part1()
    part2()

    #26362555 is too low
    #18422941
    #3719445
    #69275878
    #70478672