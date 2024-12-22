from dataclasses import dataclass
from functools import reduce
import re
import numpy as np
import math

def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines

@dataclass
class Button:
    name: str
    x: int
    y: int

def total_for_button(solution):
    answer = reduce(lambda x,y: math.ceil(x)*3 + math.ceil(y)*1, solution)
    print(answer)
    return answer

def part1():
    lines = get_input('long.txt')
    total = 0
    for l in lines:
        if 'Button A' in l:
            x = re.findall(r'X\+(\d+)', l)
            y = re.findall(r'Y\+(\d+)',l)
            A = Button('A', int(x[0]), int(y[0]))
        elif 'Button B' in l:
            x = re.findall(r'X\+(\d+)', l)
            y = re.findall(r'Y\+(\d+)',l)
            B = Button('B', int(x[0]), int(y[0]))
        elif 'Prize' in l:
            prize_x = re.findall(r'X=(\d+)', l)
            prize_y = re.findall(r'Y=(\d+)',l)
            buttons = np.array([[A.x, B.x], [A.y, B.y]])
            answers = np.array([int(prize_x[0]), int(prize_y[0])])
            solution = np.linalg.solve(buttons, answers)
            if (solution[0] > 0 ) and (solution[1] > 0 ):
                if solution[0] + solution[1] <=100:
            
            #if (solution[0] > 0 and solution[0] <= 100) and (solution[1] > 0 and solution[1] <= 100):
                    print(solution)
                    total += total_for_button(solution)

    print(total)
    #31623.69001650189 is too high
    #31551 too high
    #30391 wrong answer for 99 times
    #31191 wrong answer for soltions must also be positive
    # 31324 math.ceil still not right grrrr



def part2():
    pass

if __name__ == "__main__":
    part1()
    part2()