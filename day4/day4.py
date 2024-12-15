import numpy as np

def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines


def part1():
    # divide the input into rows
    # search the row for XMAS and SAMX
    xmas_mask = np.array(['X', 'M','A','S'])
    samx_mask = np.array(['S','A','M','X'])
    lines = get_input('short.txt')
    matrix = []
    for l in lines:
        matrix.append(list(l))

    word_search = np.array(matrix)
    for w in range(len(word_search)):
        print(word_search[w])






def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()