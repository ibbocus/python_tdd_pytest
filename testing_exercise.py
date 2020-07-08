import unittest
import math
from exercise_calc import Functions
import pytest



class Calc_Test(unittest.TestCase):

    a = Functions()

    def test_sqrt(self):
        self.assertEqual(self.a.find_sqrt(16), 4)

    def test_find_ceil(self):
        self.assertEqual(self.a.find_ceil(25.8237), 26)



#
# b = Functions
# print(b.find_sqrt(16))
#
# print(b.find_ceil(25.98450754))
