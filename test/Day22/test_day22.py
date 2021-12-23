import unittest

from puzzles.Day22.day22 import part1, part2
from test.TestConfig import TestConfig


class Day22Test(TestConfig, unittest.TestCase):
    def test_day22_part1(self):
        self.assertEqual(part1(), 581108)

    def test_day22_part2(self):
        self.assertEqual(part2(), 1325473814582641)
