import unittest

from puzzles.Day21.day21 import part1, part2
from test.TestConfig import TestConfig


class Day21Test(TestConfig, unittest.TestCase):
    def test_day21_part1(self):
        self.assertEqual(part1(), 713328)

    def test_day21_part2(self):
        self.assertEqual(part2(), 92399285032143)
