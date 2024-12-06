import numpy as np
from numpy import ndarray

def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines


def isSafe(report: ndarray[int])->bool:
    levels = np.diff(report)
    print(levels)
    all_positive = np.all(levels > 0)
    all_negative = np.all(levels < 0)
    in_bounds = np.all((levels <= 3)& (levels >= -3))
    # print(all_decreasing, all_increasing, in_bounds)
    if not in_bounds:
        print('returning not in bounds')
        return False

    print('all neg or all pos ', all_negative or all_positive)
    return all_negative or all_positive
    print('returning false')


    print('returning true')
    return True



def part1():
    safe_reports = 0
    lines = get_input('long.txt')
    for l in lines:
        report = np.array(list(map(int, l.split())))
        if isSafe(report):        
            safe_reports = safe_reports + 1

    print('safe reports: ', safe_reports)


def part2():
    pass

if __name__ == "__main__":
    part1()