import numpy as np
from numpy import ndarray

def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines


def isSafe(report: ndarray[int])->bool:
    levels = np.diff(report)
    all_positive = np.all(levels > 0)
    all_negative = np.all(levels < 0)
    in_bounds = np.all((levels <= 3)& (levels >= -3))
    # print(all_decreasing, all_increasing, in_bounds)
    if not in_bounds:
        return False

    return all_negative or all_positive


def part1():
    safe_reports = 0
    s = []
    lines = get_input('long.txt')
    for l in lines:
        report = np.array(list(map(int, l.split())))
        if isSafe(report):        
            safe_reports = safe_reports + 1
            s.append(report)

    print('part 1 safe reports: ', safe_reports)


def _remove_one_element(report, position):
        report = report.tolist()
        if position == 0:
            return report[1:]
        if position == len(report):
            return report[0:position-1]
        return report[0:position] + report[position+1:]

def part2():
    safe_reports = []
    unsafe_reports = []
    lines = get_input('long.txt')
    for l in lines:
        report = np.array(list(map(int, l.split())))
        if isSafe(report):
            safe_reports.append(report) 
        else:
            unsafe_reports.append(report)
    print('safe: ', len(safe_reports))

    for un in unsafe_reports:
        for i in range(len(un)):
            maybe_safe = _remove_one_element(un, i)
            if isSafe(maybe_safe):
                # print('maybe_safe: ', maybe_safe)
                safe_reports.append(un)
                break
            # else:
                # print('unsafe: ', maybe_safe)


    print(f"part2 safe: {len(safe_reports)} unsafe: {len(unsafe_reports)}")
    # 529 is too low
    # 583 is too high

if __name__ == "__main__":
    part1()
    part2()