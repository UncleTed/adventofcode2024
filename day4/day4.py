import numpy as np

def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines

xmas_mask = 'XMAS'
samx_mask = 'SAMX'

def horizontally(matrix):
    row_counter = 0
    for row in matrix:
        if xmas_mask in ''.join(row):
            row_counter +=1

        if samx_mask in ''.join(row):
            row_counter += 1
    return row_counter

def vertially(matrix):
    transpose = np.array(matrix).T
    print(transpose)
    return horizontally(transpose)

def diagonally(matrix):
    pass
# figure out how to slice diagonally with lenghth => 4
# (3,0) -> (0,3) =
    # (3,3), (2,2), (1,1)


def part1():
    # divide the input into rows
    # search the row for XMAS and SAMX

    lines = get_input('short.txt')
    matrix = []
    for l in lines:
        matrix.append(list(l))
    print(matrix)

    horitonalFinds = horizontally(matrix)
    verticalFinds = vertially(matrix)

    print(f"found horizontal {horitonalFinds}")
    print(f"found veritcal {verticalFinds}")

def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()