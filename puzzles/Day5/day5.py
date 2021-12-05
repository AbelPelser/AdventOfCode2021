from collections import defaultdict

from util import *


def part1():
    lines = read_input_as_lines()
    covered = defaultdict(int)
    for line in lines:
        coord_a, coord_b = line.split(' -> ')
        a_x, a_y = coord_a.split(',')
        b_x, b_y = coord_b.split(',')
        a_x = int(a_x)
        a_y = int(a_y)
        b_x = int(b_x)
        b_y = int(b_y)
        if a_x == b_x:
            for i in range(min(a_y, b_y), max(a_y, b_y) + 1):
                covered[(a_x, i)] += 1
        if a_y == b_y:
            for i in range(min(a_x, b_x), max(a_x, b_x) + 1):
                covered[(i, a_y)] += 1
        # vectors[(int(a_x), int(a_y))] = (int(b_x), int(b_y))
    return len({s for s in covered.keys() if covered[s] >= 2})


def part2():
    lines = read_input_as_lines()
    covered = defaultdict(int)
    for line in lines:
        coord_a, coord_b = line.split(' -> ')
        a_x, a_y = coord_a.split(',')
        b_x, b_y = coord_b.split(',')
        a_x = int(a_x)
        a_y = int(a_y)
        b_x = int(b_x)
        b_y = int(b_y)
        if a_x == b_x:
            for i in range(min(a_y, b_y), max(a_y, b_y) + 1):
                covered[(a_x, i)] += 1
        elif a_y == b_y:
            for i in range(min(a_x, b_x), max(a_x, b_x) + 1):
                covered[(i, a_y)] += 1
        else:
            d_x = 1 if a_x < b_x else -1
            d_y = 1 if a_y < b_y else -1
            while a_x != b_x and a_y != b_y:
                covered[(a_x, a_y)] += 1
                a_x += d_x
                a_y += d_y
            covered[(a_x, a_y)] += 1
        # vectors[(int(a_x), int(a_y))] = (int(b_x), int(b_y))
    return len({s for s in covered.keys() if covered[s] >= 2})


if __name__ == '__main__':
    print(part1())
    print(part2())
