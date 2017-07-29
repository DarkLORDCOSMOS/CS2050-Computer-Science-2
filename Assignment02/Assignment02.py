from __future__ import print_function
import unittest

'''
Description: CS2050 Assignment 2 - Dictionaries
Author: John Samson
Version: Python 3.6 (32-bit)
Help provided to: 
Help received from: David Faller, Nicole Weickert, N. Barnes
'''

'''
    Implement a dictionary using chaining.
    You may assume every key has a hash() method, e.g.:
    >>> hash(1)
    1
    >>> hash('hello world')
    -2324238377118044897
'''

class dictionary:
    def __init__(self, init=None):
        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0
        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        return self.__count

    def __flattened(self):
        return [item for inner in self.__items for item in inner]

    def __iter__(self):
        return(iter(self.__flattened()))

    def __str__(self):
        return(str(self.__flattened()))

    # Add to the dictionary.
    def __setitem__(self, key, value):
        hash_key = hash(key) % self.__limit
        if self.__items[hash_key] == []:
            self.__items[hash_key].append([key, value])
            self.__count += 1
            if self.__count > (self.__limit * 3) // 4:
                self.__rehash__()
            return
        # Add to existing hash location
        else:
            for item in self.__items[hash_key]:
                if key == item[0]:
                    item[1] = value
                    # self.__count += 1
                    return
        self.__items[hash_key].append([key, value])
        self.__count += 1
        # Rehash if load > 75%
        if self.__count > (self.__limit * 3) // 4:
            self.__rehash__()

    # Retrieve from the dictionary
    def __getitem__(self, key):
        tmp = []
        hash_key = hash(key) % self.__limit
        for item in self.__items[hash_key]:
            if key == item[0]:
                tmp = item[1]
            else:
                for inner in item:
                    print(key)
                    if key == inner:
                        tmp = inner[1]
        return tmp

    # Implements the 'in' operator.
    def __contains__(self, key):
        hash_key = hash(key)% self.__limit
        for key in self.__items:
            if self.__items[hash_key] != None:
                tmp = True
            else:
                tmp = False
        return tmp

    # Rehashing when load goes over 75% or below 25%
    def __rehash__(self):
        tmp = self.__items
        if self.__count > (self.__limit * 3)//4:
            self.__limit *= 2
        elif self.__count < (self.__limit)//4:
            self.__limit //= 2
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0
        for i in tmp:
            if i == None:
                return self.__limit
            for j in i:
                self.__setitem__(j[0], j[1])
        return self.__limit

    # Delete item
    def __delitem__(self, key):
        hash_key = hash(key)% self.__limit
        tmp = []
        hash_key = hash(key) % self.__limit
        for item in self.__items[hash_key]:
            if key == item[0]:
                self.__items[hash_key] = None
                self.__count -= 1
            else:
                for inner in item:
                    if key == inner[0]:
                        inner = []
                        self.__count -= 1
        if self.__count < (self.__limit // 4):
            self.__rehash__()
        return

    # Return keys
    def __keys__(self):
        tmp = []
        for item in self.__items:
            for inner in item:
                tmp += [inner[0]]
        return tmp

    # Return values
    def __values__(self):
        tmp = []
        for item in self.__items:
            for inner in item:
                tmp += [inner[1]]
        return tmp

    # Test if equal
    def __eq__(self, other):
        for self_item in self.__items:
            for self_inner in self_item:
                for other_item in other.__items:
                    for other_inner in other_item:
                        if other_inner == self_inner:
                            return True
                        else:
                            return False

    # Return items
    def __items__(self):
        tmp = []
        for item in self.__items:
            for inner in item:
                tmp += [(inner[0], inner[1])]
        return tmp

''' C-level work
'''
class test_add_two(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")

class test_add_twice(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[1] = "one"
        self.assertEqual(len(s), 1)
        self.assertEqual(s[1], "one")

class test_store_false(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = False
        self.assertTrue(1 in s)
        self.assertTrue(1 in s)
        self.assertFalse(s[1])

class test_store_none(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = None
        self.assertTrue(1 in s)
        self.assertEqual(s[1], None)

class test_none_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[None] = 1
        self.assertTrue(None in s)
        self.assertEqual(s[None], 1)

class test_False_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[False] = 1
        self.assertTrue(False in s)
        self.assertEqual(s[False], 1)

class test_collide(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[10] = "ten"
        self.assertEqual(len(s), 2)
        self.assertTrue(0 in s)
        self.assertTrue(10 in s)

''' B-level work
    Add doubling and rehashing when load goes over 75%
    Add __delitem__(self, key)
'''

# Doubling and rehashing when load goes over 75%
class test_double(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        self.assertEqual(s._dictionary__limit, 10)
        s[6] = "six"
        s[7] = "seven"
        self.assertEqual(s._dictionary__limit, 20)
        s[8] = "ocho"
        s[9] = "nine"
        s[10] = "ten"
        s[11] = "eleven"
        s[12] = "twelve"
        s[13] = "thirteen"
        self.assertEqual(s[1], "one")
        self.assertEqual(s[11], "eleven")
        self.assertTrue(s.__len__(), 14)
        self.assertEqual(s._dictionary__limit, 20)

# Delete item
class test_delete(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s.__delitem__(0)
        s.__delitem__(4)
        self.assertTrue(s.__len__(), 3)
        self.assertFalse(0 in s)
        self.assertTrue(4 not in s)

''' A-level work
    Add halving and rehashing when load goes below 25%
    Add keys()
    Add values()
'''

# halving and rehashing when load goes below 25%
class test_halve(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s.__delitem__(4)
        s.__delitem__(3)
        s.__delitem__(2)
        self.assertEqual(s._dictionary__limit, 10)
        s.__delitem__(1)
        self.assertEqual(s[0], "zero")
        self.assertTrue(s.__len__(), 1)
        self.assertEqual(s._dictionary__limit, 5)

# Return keys
class test_keys(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        self.assertEqual(s.__keys__(), [1, 2, 3])

# Return values
class test_values(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        self.assertEqual(s.__values__(), ["one", "two", "three"])

''' Extra credit
    Add __eq__()
    Add items(), returns a list of tuples "a list of D's (key, value) pairs, as 2-tuples"
'''

# Test if (key, value) pair in two dictionaries
class test_equal(unittest.TestCase):
    def test(self):
        a = dictionary()
        a[0] = "zero"
        a[1] = "one"
        a[2] = "two"
        a[3] = "three"
        a[4] = "four"
        a[14] = "fourteen"
        b = dictionary()
        b[0] = "zero"
        b[2] = "two"
        b[4] = "four"
        b[6] = "six"
        b[8] = "eight"
        b[14] = "fourteen"
        self.assertTrue(a.__eq__(b), True)
        self.assertTrue(b.__eq__(a), True)

# Return items
class test_items(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        self.assertEqual(s.__items__(), [(1, "one"), (2, "two"), (3, "three")])

# Test chaining
class test_chain(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[11] = "eleven"
        s[21] = "twenty-one"
        s[31] = "thirty-one"
        s[51] = "fifty-one"
        s[71] = "seventy-one"
        self.assertEqual(s[51], "fifty-one")

if '__main__' == __name__:
    unittest.main()
