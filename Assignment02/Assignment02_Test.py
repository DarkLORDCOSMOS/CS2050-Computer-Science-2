from __future__ import print_function
import unittest


class test_add_two(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], 1)
        self.assertEqual(s[2], 2)

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


unittest.main()
