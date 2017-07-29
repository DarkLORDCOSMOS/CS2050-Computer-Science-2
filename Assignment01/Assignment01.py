from __future__ import print_function
import unittest

''' when run with "-m unittest", the following produces:
    FAILED (failures=9, errors=2)
    your task is to fix the failing tests by implementing the necessary
    methods. '''

class LinkedList(object):
    class Node(object):
        # pylint: disable=too-few-public-methods
        ''' no need for get or set, we only access the values inside the
            LinkedList class. and really, never have setters. '''
        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def __init__(self, initial=None):
        self.front = self.back = self.current = None
        if initial != None:
            for item in initial:
                item = item.__str__()
                self.push_front(item)

    def empty(self):
        return self.front == self.back == None

    def __str__(self):
        tmp = ""
        current_node = self.front
        while current_node != self.back:
            tmp += self.pop_back() + ", "
        tmp += self.pop_back()
        return tmp

    def __repr__(self):
        tmp = "LinkedList(("
        current_node = self.front
        while current_node != self.back:
            tmp += self.pop_back() + ", "
        tmp += self.pop_back() + "))"
        return tmp

    def __iter__(self):
        self.current = self.front
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next_node
            return tmp
        else:
            raise StopIteration()

    def push_front(self, value):
        new = self.Node(value, self.front)
        if self.empty():
            self.front = self.back = new
        else:
            self.front = new

    ''' you need to(at least) implement the following three methods'''
    def pop_front(self):
        if self.empty():
            raise RuntimeError
        tmp = self.front.value
        if self.front == self.back:
            self.front = self.back = None
        else:
            self.front = self.front.next_node
        return tmp

    def push_back(self, value):
        new = self.Node(value, self.back)
        if self.empty():
            self.back = self.front = new
        elif self.back == self.front:
            self.back = new
            self.front.next_node = self.back
        else:
            self.back.next_node = new
            self.back = new
        self.back.next_node = None

    def pop_back(self):
        if self.empty():
            raise RuntimeError
        tmp = self.back.value
        if self.front == self.back:
            self.back = self.front = None
        else:
            current_node = self.front
            while current_node.next_node != None:
                if current_node.next_node == self.back:
                    self.back = current_node
                current_node = current_node.next_node
        return tmp

    def pop_value(self, value):
        tmp = self.front.value
        if self.empty():
            raise RuntimeError
        elif self.front == self.back:
            if self.front.value == value:
                self.back = self.front = None
        elif self.front.next_node == self.back:
            if self.front.value == value:
                self.front = self.back
            elif self.back.value == value:
                tmp = self.back.value
                self.back = self.front
        else:
            current_node = self.front
            while current_node.next_node != None:
                if self.front.value == value:
                    self.front = self.front.next_node
                elif current_node.next_node.value == self.back.value == value:
                    tmp = self.back.value
                    self.back = current.node
                elif current_node.next_node.value == value:
                    tmp = current_node.next_node.value
                    current_node.next_node = current_node.next_node.next_node
                current_node = current_node.next_node
        return tmp

    # Extra Credit #1
    def __del__(self, value):
        if self.empty():
            raise RuntimeError
        elif self.front == self.back:
            if self.front.value == value:
                self.back = self.front = None
        elif self.front.next_node == self.back:
            if self.front.value == value:
                self.front = self.back
            elif self.back.value == value:
                self.back = self.front
        else:
            current_node = self.front
            while current_node.next_node != None:
                if self.front.value == value:
                    self.front = self.front.next_node
                elif current_node.next_node.value == self.back.value == value:
                    self.back = current.node
                elif current_node.next_node.value == value:
                    current_node.next_node = current_node.next_node.next_node
                current_node = current_node.next_node
        return

    # Extra Credit #2
    def __mid__(self):
        if self.empty():
            raise RuntimeError
        tmp = self.front.value
        current_node = self.front
        middle_node = self.front
        while current_node.next_node != None:
            current_node = current_node.next_node.next_node
            middle_node = middle_node.next_node
            tmp = middle_node.value
        return tmp

''' C-level work '''
class TestEmpty(unittest.TestCase):
    def test(self):
        self.assertTrue(LinkedList().empty())

class TestPushFrontPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), 3)
        self.assertTrue(linked_list.empty())

class TestPushFrontPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertTrue(linked_list.empty())

class TestPushBackPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertTrue(linked_list.empty())

class TestPushBackPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back("foo")
        linked_list.push_back([3, 2, 1])
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), [3, 2, 1])
        self.assertEqual(linked_list.pop_back(), "foo")
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertTrue(linked_list.empty())

''' B-level work '''
class TestInitialization(unittest.TestCase):
    def test(self):
        linked_list = LinkedList(("one", 2, 3.141592))
        self.assertEqual(linked_list.pop_back(), "one")
        self.assertEqual(linked_list.pop_back(), "2")
        self.assertEqual(linked_list.pop_back(), "3.141592")

class TestStr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__str__(), '1, 2, 3')

''' A-level work '''
class TestRepr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__repr__(), 'LinkedList((1, 2, 3))')

class TestErrors(unittest.TestCase):
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_front())
    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_back())

''' write some more test cases. '''
class TestPopValue(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 7, 15))
        self.assertEqual(linked_list.pop_value("2"), "2")
        self.assertEqual(linked_list.pop_value("7"), "7")
        self.assertEqual(linked_list.pop_value("15"), "15")
        self.assertEqual(linked_list.pop_value("1"), "1")
        self.assertTrue(linked_list.empty())

''' extra credit. 
    - write test cases for and implement a delete(value) method.'''
class TestDelete(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back("hi")
        linked_list.push_back("how")
        linked_list.push_back("are")
        linked_list.push_back("you")
        linked_list.push_back("goodbye")
        linked_list.__del__("you")
        linked_list.__del__("hi")
        linked_list.__del__("how")
        linked_list.__del__("are")
        linked_list.__del__("goodbye")
        self.assertTrue(linked_list.empty())

''' - write test cases for and implement a method that finds the middle
    element with only a single traversal.'''
class TestMiddleEven(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 6, 12, 14, 15, 28, 37, 56))
        self.assertEqual(linked_list.__mid__(), ('15', '14'))

class TestMiddleOdd(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 6, 12, 15, 28))
        self.assertEqual(linked_list.__mid__(), '12')

''' the following is a demonstration that uses our data structure as a
    stack'''

def fact(number):
    '''"Pretend" to do recursion via a stack and iteration'''

    if number < 0: raise ValueError("Less than zero")
    if number == 0 or number == 1: return 1

    stack = LinkedList()
    while number > 1:
        stack.push_front(number)
        number -= 1

    result = 1
    while not stack.empty():
        result *= stack.pop_front()

    return result

class TestFactorial(unittest.TestCase):
    def test_less_than_zero(self):
        self.assertRaises(ValueError, lambda: fact(-1))
    def test_zero(self):
        self.assertEqual(fact(0), 1)
    def test_one(self):
        self.assertEqual(fact(1), 1)
    def test_two(self):
        self.assertEqual(fact(2), 2)
    def test_10(self):
        self.assertEqual(fact(10), 10*9*8*7*6*5*4*3*2*1)

if '__main__' == __name__:
    unittest.main()