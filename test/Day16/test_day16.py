import unittest

from puzzles.Day16.day16 import part1, part2
from test.TestConfig import TestConfig


class Day16Test(TestConfig, unittest.TestCase):
    def test_day16_part1(self):
        self.assertEqual(part1(), 893)

    def test_day16_part2(self):
        self.assertEqual(part2(), 4358595186090)
