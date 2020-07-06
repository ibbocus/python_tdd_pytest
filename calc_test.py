import pytest
import unittest
from calc import Calc


class calc_test(unittest.TestCase):
    simple_calc = Calc() # creating an object of the Calc class

    def test_add(self):
        self.assertEqual(self.simple_calc.addition(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.simple_calc.subtraction(10, 6), 4)

    def test_multiply(self):
        self.assertEqual(self.simple_calc.multiply(5, 10, 7, 2, 6), 4200)

    def test_divide(self):
        self.assertEqual(self.simple_calc.divide(100, 2, 5, 5), 2)

    def test_modulo(self):
        self.assertEqual(self.simple_calc.modulo(25, 50), 0) # Larger number to go second






# simple calc is the object we have created with the test of (self.simple_calc.add(2, 2), 4) which tests to see whether 2 + 2 = 4
# We write this test with an empty calc file to ensure its failure - so that we can refactor and code it to pass.
# It is important, when testing, to start with a failure and move to a pass through iterations.
# This is good because we want to test s we go along
