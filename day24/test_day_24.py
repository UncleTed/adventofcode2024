import unittest

from day24.today import Connection, and_gate, find_wire, wire, xor_gate


class TestDay24(unittest.TestCase):
    def test_calculate(self):
        wire1 = wire('x00', 1)
        wire2 = wire('y00', 0)
        output = wire('z00', None)

        c = Connection(wire1, wire2, and_gate, output)
        c.calculate()
        self.assertEqual(0, output.value)

    def test_xor(self):
        self.assertEqual(1 ^ 1, 0)
        self.assertEqual(1 ^ 0, 1)
        self.assertEqual(xor_gate(wire('a', 1), wire('b',1)), 0)
        self.assertEqual(xor_gate(wire('c',0), wire('d', 1)), 1)
        self.assertEqual(xor_gate(wire('a', None), wire('b', None)), 0)

    def test_find_wire(self):
        wire1 = wire('x00', 1)
        wire2 = wire('y00', 0)
        wire3 = wire('abc', 1)

        actual_wire = find_wire([wire1, wire2, wire3], 'abc')
        self.assertEqual(wire3, actual_wire)
        actual_wire = find_wire([wire3, wire2, wire1], 'x00')
        self.assertEqual(wire1, actual_wire)
        