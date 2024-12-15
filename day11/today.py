from dataclasses import dataclass

from list_node import StraightLine, Stone


def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines


def _has_even_number_of_digits( stone: Stone)-> bool:
    return len(str(stone.value)) % 2


def blink(linked_list: StraightLine):
    current = linked_list.head
    while(current is not None):
        if current.value == 0:
            current.value = 1
            current = current.next
        elif _has_even_number_of_digits(current):
            current = current.next
        else:
            current.value = current.value * 2024
            current = current.next



def part1():
    straight_line = StraightLine() 
    lines = get_input('short.txt')
    for value in lines[0].split(' '):
        straight_line.insert_at_end(value)

    blink(straight_line)
    print(straight_line.traverse())


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()