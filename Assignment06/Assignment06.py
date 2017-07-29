from __future__ import print_function
import unittest, sys


'''
Description: N-Queens Recursive 'Brute Force' Algorithm
Author: John Samson
Version: Python 3.6
Help received from: Nick Barnes, David Faller, Mike Lacroix
Help provided to: Nick Barnes, David Faller, Mike Lacroix, Ahern Nelson
'''

'''
    Given the location of two queens, find if they are safe
    from each other.
'''

def safe(one, two):
    if one[0] == two[0]: return False
    if one[1] == two[1]: return False
    if abs(two[0]-one[0]) == abs(two[1]-one[1]): return False
    return True

def print_solution(size, solutions):
    print("for:", size)
    if solutions == []:
        print("no solution found")
        return

    print('-' * size)

    for placed in solutions:
        for i in range(size):
            for j in range(size):
                if [i, j] in placed:
                    sys.stdout.write("Q")
                else:
                    sys.stdout.write(".")
            print()

        print('-' * size)

    print(len(solutions), "solutions found")

def solve(size, row, placed, solutions):
    # If the row is greater than the size of the board, we're done
    if row == size:
        solutions.append(placed)
        return

    # Go through the columns in this row
    for column in range(size):

        # Go through all the already placed queens and see if
        #   placing a new queen at (row, column) is safe
        is_safe = True
        for queen in placed:
            if is_safe and not safe([row, column], queen):
                is_safe = False
                break

        # If it is
        if is_safe:
            solve(size, row + 1, placed + [[row, column]], solutions)
    return solutions

class test_Queens(unittest.TestCase):
    def test_safe(self):
        self.assertTrue(safe([0, 1], [3, 2]))
        self.assertTrue(safe([2, 4], [3, 6]))
        self.assertTrue(safe([3, 3], [2, 7]))
        self.assertTrue(safe([5, 0], [4, 2]))
    def test_unsafe(self):
        self.assertFalse(safe([1, 1], [1, 2]))
        self.assertFalse(safe([1, 1], [4, 4]))
        self.assertFalse(safe([0, 3], [1, 3]))
        self.assertFalse(safe([5, 0], [4, 1]))
    def test_solution(self):
        solutions = solve(4, 0, [], [])
        self.assertTrue([[0, 2], [1, 0], [2, 3], [3, 1]] in solutions)
        solutions = solve(6, 0, [], [])
        self.assertTrue([[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]] in solutions)
        solutions = solve(8, 0, [], [])
        self.assertTrue([[0, 0], [1, 6], [2, 3], [3, 5], [4, 7], [5, 1], [6, 4], [7, 2]] in solutions)
    def test_03(self):
        solutions = solve(3, 0, [], [])
        self.assertEquals(len(solutions), 0)
        print_solution(3, solutions)
    def test_04(self):
        solutions = solve(4, 0, [], [])
        self.assertEquals(len(solutions), 2)
        print_solution(4, solutions)
    def test_05(self):
        solutions = solve(5, 0, [], [])
        self.assertEquals(len(solutions), 10)
        print_solution(5, solutions)
    def test_06(self):
        solutions = solve(6, 0, [], [])
        self.assertEquals(len(solutions), 4)
        print_solution(6, solutions)
    def test_07(self):
        solutions = solve(7, 0, [], [])
        self.assertEquals(len(solutions), 40)
        print_solution(7, solutions)
    def test_08(self):
        solutions = solve(8, 0, [], [])
        self.assertEquals(len(solutions), 92)
        print_solution(8, solutions)
    def test_09(self):
        solutions = solve(9, 0, [], [])
        self.assertEquals(len(solutions), 352)
    def test_10(self):
        solutions = solve(10, 0, [], [])
        self.assertEquals(len(solutions), 724)
    def test_11(self):
        solutions = solve(11, 0, [], [])
        self.assertEquals(len(solutions), 2680)

# For extra credit, have your program solve the problem of any size.
# For extra-extra credit, have your program find all the solutions of
# a given size; for example, there are 92 solutions for eight queens.
