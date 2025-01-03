from dataclasses import dataclass


def get_input(file_name):
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    return lines


@dataclass
class wire:
    name: str
    value: int

    def __repr__(self):
        return f'{self.name} : {self.value}'


class Connection:
    def __init__(self, wire1: wire, wire2: wire, operation: any, output: wire):
        self.wire1 = wire1
        self.wire2 = wire2
        self.operation = operation
        self.output = output

    def calculate(self)->bool:
        try:
            self.output.value = self.operation(self.wire1, self.wire2)
            return True
        except Exception as e:
            print('----------------------' ,self)
            return False
    
    def __repr__(self):
        return f'{self.wire1} {self.operation} {self.wire2} -> {self.output}'

def and_gate(a: wire,b: wire) -> int:
    return a.value and b.value

def or_gate(a:wire , b: wire)-> int:
    return a.value or b.value

def xor_gate(a:wire, b:wire)->int:
    return a.value ^ b.value

def find_wire(wires: list[wire], name: str)->wire:
    for w in wires:
        if w.name == name:
            return w
    return None

def run_all_calculation(connections: list[Connection]):

    # do the x and y first which will solve some 
    # do the ones that aren;t solved
    # two lists: solved and unsolved
    # x and y dont' have seem to have values
    do_it_again = True
    while do_it_again:
        do_it_again = False
        for c in connections:
            result = c.calculate()
            if result == False:
                print(c)
                do_it_again = True
            


def part1():
    wires = []
    connections: list[Connection] = list()
    lines = get_input('medium.txt')
    for l in lines:
        if ":" in l:
            wires.append(wire(l.split(":")[0], int(l.split(":")[1])))
        if "->" in l:
            wire1, operator, wire2, _, output = l.split()
            if operator == "AND":
                operator = and_gate
            elif operator == "OR":
                operator = or_gate
            elif operator == "XOR":
                operator = xor_gate
            first_wire = wire(wire1, None)
            if wire1 in wires:
                first_wire = find_wire(wires, wire1)


            second_wire = wire(wire2, None)
            if wire2 in wires:
                second_wire = find_wire(wires, wire2)
            output_wire = wire(output, None)
            wires.append(output_wire)
            connections.append(Connection(first_wire, second_wire,operator, output_wire))

    connections.sort(key=lambda x: x.output.name, reverse=False)
    # print([c for c in connections])
    print(wires)

    # run_all_calculation(connections)

    bits = [w.value for w in wires if w.name.startswith('z')]
    bits.reverse()
    print(int(''.join(map(str, bits)),2))


def part2():
    pass

if __name__ == "__main__":
    part1()
    part2()