import unittest

from day11.list_node import StraightLine, Stone
from day11.today import blink



class TestLinkedList(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(1, 1)

    def test_list_node(self):
        first_node = Stone(1)
        self.assertIsNone(first_node.next)
        self.assertIsNone(first_node.prev)
        self.assertEqual(first_node.value, 1)

        second_node = Stone(2)
        first_node.next = second_node

        self.assertEqual(first_node.next, second_node)

    def test_insert(self):
        linked_list = StraightLine()
        linked_list.insert_at_beginning(1)
        self.assertEqual("1", linked_list.traverse())
        linked_list.insert_at_beginning( 2)
        linked_list.insert_at_beginning(3)
        self.assertEqual("3 2 1", linked_list.traverse())

    def test_insert_at_beginning_with_empty_list(self):
        linked_list = StraightLine()
        head = linked_list.insert_at_beginning( 1)
        self.assertEqual("1", linked_list.traverse())
        for i in range(10):
            linked_list.insert_at_beginning(i)
        self.assertEqual("9 8 7 6 5 4 3 2 1 0 1", linked_list.traverse())

    def test_linked_list_head(self):
        linked_list = StraightLine()
        self.assertIsNone(linked_list.head)
        linked_list.insert_at_beginning(1)
        self.assertEqual(1, linked_list.head.value)

    def test_insert_at_end(self):
        linked_list = StraightLine()
        linked_list.insert_at_end(1)
        self.assertEqual("1", linked_list.traverse())
        linked_list.insert_at_end(2)
        linked_list.insert_at_end(3)
        linked_list.insert_at_end(4)

        self.assertEqual("1 2 3 4", linked_list.traverse())

    def test_insert_in_the_middle(self):
        linked_list = StraightLine()
        for i in range(10):
            linked_list.insert_at_end(i)
        linked_list.insert_in_middle(5, 24)
        self.assertEqual("0 1 2 3 4 5 24 6 7 8 9", linked_list.traverse())

    def test_blink(self):
        linked_list = StraightLine()
        linked_list.insert_at_end(0)
        linked_list.insert_at_end(1)
        linked_list.insert_at_end(10)
        linked_list.insert_at_end(99)
        linked_list.insert_at_end(999)
        expected = "1 2024 1 0 9 9 2021976"
        blink(linked_list)
        self.assertEqual(expected, linked_list.traverse())

    def test_split_stone(self):
        straight_line = StraightLine()
        straight_line.insert_at_end(1)
        straight_line.insert_at_end(2)
        straight_line.insert_at_end(3)

        two_stone = straight_line.head.next
        straight_line.split(two_stone, '2024')
        expected = "1 20 24 3"
        self.assertEqual(expected, straight_line.traverse())    

    def test_another_example_6_blinks(self):
        straight_line = StraightLine()
        straight_line.insert_at_beginning(125)
        straight_line.insert_at_end(17)
        blink(straight_line)
        self.assertEqual("253000 1 7", straight_line.traverse())
        blink(straight_line)
        self.assertEqual("253 0 2024 14168", straight_line.traverse())
        blink(straight_line)
        self.assertEqual("512072 1 20 24 28676032", straight_line.traverse())   
        blink(straight_line)
        self.assertEqual("512 72 2024 2 0 2 4 2867 6032", straight_line.traverse()) 
        blink(straight_line)
        self.assertEqual("1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32", straight_line.traverse())     
        blink(straight_line)
        expected = "2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"
        self.assertEqual(expected, straight_line.traverse())  
        self.assertEqual(len(expected.split(' ')),22)
        self.assertEqual(22, straight_line.size())

    def test_25_blinks(self):
        straight_line = StraightLine()
        straight_line.insert_at_beginning(125)
        straight_line.insert_at_end(17)
        for i in range(25):
            blink(straight_line)
        self.assertEqual(55312, straight_line.size())


            
