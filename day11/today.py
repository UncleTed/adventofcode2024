from dataclasses import dataclass

from list_node import StraightLine, Stone
import time
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from cProfile import Profile
from pstats import SortKey, Stats

#92395903033322543477554551 


def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines


def _has_even_number_of_digits( stone: Stone)-> bool:
    return len(stone.value) % 2 == 0


def blink(straight_line: StraightLine):
    current = straight_line.head
    while(current is not None):
        if current.value == '0':
            current.value = '1'
            current = current.next
        elif _has_even_number_of_digits(current):
            split_stone = straight_line.split(current, current.value)
            current = split_stone.next
        else:
            current.value = str(int(current.value) * 2024)
            current = current.next



def part1():
    straight_line = StraightLine() 
    lines = get_input('long.txt')
    for value in lines[0].split(' '):
        straight_line.insert_at_end(value)

    for i in range(25):
        tic = time.perf_counter()
        blink(straight_line)
        toc = time.perf_counter()
        print(f"blink[{i}]: {toc - tic}")
    print(straight_line.size())
    # 38_253 is too low
    # 190865
    # 311_887 is too high



def timing_graph():
    input = get_input('timing')
    timing = [t.split(' ') for t in input]
    x = [int(t[0]) for t in timing]
    y = [float(t[1]) for t in timing]
    plt.scatter(x, y, marker='.')
    plt.ylabel('seconds')
    plt.xlabel('iterations')
    plt.show()


def part2():
    straight_line = StraightLine() 
    lines = get_input('long.txt')
    for value in lines[0].split(' '):
        straight_line.insert_at_end(value)

    for i in range(37):
        tic = time.perf_counter()
        blink(straight_line)
        toc = time.perf_counter()
        print(f"{i} {toc - tic} ")
    print("Part 2 : ",straight_line.size())
    with open('37_out.txt', 'w') as out_file:
        out_file.write(straight_line.traverse())


if __name__ == "__main__":
    # part1()
    # part2()
    with Profile() as profile:
        print(f"{part2() } ")
        Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats()
         
         
    # timing_graph()