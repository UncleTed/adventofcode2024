from dataclasses import dataclass
from enum import Enum


def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines

class Compass(Enum):
    E = 1
    W = 2
    N = 3
    S = 4

@dataclass
class Direction:
    x: int
    y: int
    viz: str

East = Direction(0,1, '>')
West = Direction(0,-1, '<')
North = Direction(-1,0, '^')
South = Direction(1,0, '~')


@dataclass
class Reindeer:
    x: int
    y: int
    direction: Direction

    def move( self):
        self.x += self.direction.x
        self.y += self.direction.y
        maze[self.x][self.y] = self.direction.viz
    
    def get_position(self):
        return (self.x, self.y)

    def can_move(self) -> bool:
        return maze[self.x+self.direction.x][self.y+self.direction.y] != '#'
    
    def turn(self):
        if self.direction == North:
            self.direction = East
        elif self.direction == East:
            self.direction = South
        elif self.direction == South:
            self.direction = West
        else:
            self.direction = North



maze = []


def part1():
    blitzen = Reindeer(13,1, East)

    for line in get_input('short.txt'):
        maze.append(list(line))


    for i in range(19):
        if blitzen.can_move():
            blitzen.move()
            print(i)
            print_maze(maze)
        else:
            blitzen.turn()

       
    print(blitzen)

def part2():
    pass


def print_maze(maze):
    for i in range(len(maze)):

        print("".join(maze[i]))


if __name__ == "__main__":
    part1()
    part2()