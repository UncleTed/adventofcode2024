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
        


            
